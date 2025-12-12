from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_mysqldb import MySQL
from flask_socketio import SocketIO
from flaskwebgui import FlaskUI
import os
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

app.secret_key = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "ppe_detection"

mysql = MySQL(app)


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()
        if user:
            user_obj = User(user[0])
            login_user(user_obj)
            return redirect(url_for('Home'))
        else:
            error = "Invalid credentials"
    return render_template("login.html", error=error)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
@login_required
def Home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ppe_detection ORDER BY time DESC")
    fetchdata = cur.fetchall()

    total = cur.rowcount

    cur.close()
    totalcam1 = sum(1 for row in fetchdata if row[4] == 'Cam 1')
    totalcam2 = sum(1 for row in fetchdata if row[4] == 'Cam 2')
    totalcam3 = sum(1 for row in fetchdata if row[4] == 'Cam 3')
    # Ubah setiap baris data menjadi dictionary
    data = []
    for row in fetchdata:
        data.append({'id': row[0], 'image': row[1],
                    'time': row[2], 'classes': row[3], 'position': row[4]})

    return render_template("home.html", data=data, total=total, cam1=totalcam1, cam2=totalcam2, cam3=totalcam3)


@app.route('/form', methods=['GET'])
@login_required
def form():
    return render_template("form.html")


@app.route('/formpost', methods=['POST'])
def formpost():
    file = request.files['file']
    classes = request.form.get('classes')
    position = request.form.get('position')
    filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
    file.save(os.path.join('static/images', filename))
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO ppe_detection (image, classes, position) VALUES (%s, %s, %s)",
                (filename, classes, position))
    mysql.connection.commit()
    cur.close()
    socketio.emit('newdata', {'data': 'New data available'})
    return "success"


if __name__ == "__main__":
    # ui = FlaskUI(app=app, server="flask", width=1300, height=700, port=54321)
    ui = app.run(debug=True)
    app.run(debug=True)

    # app.secret_key = 'supersecretkey'
    # ui.run()
    # socketio.run(app)
