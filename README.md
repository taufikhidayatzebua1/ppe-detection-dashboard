# PPE Detection Web Application

A Flask-based web application for Personal Protective Equipment (PPE) detection monitoring system. This application provides real-time tracking and management of PPE detection data from multiple camera positions.

## Features

- 🔐 **User Authentication**: Secure login system with Flask-Login
- 📊 **Real-time Monitoring**: Live data updates using WebSocket (SocketIO)
- 📷 **Multi-Camera Support**: Track PPE detection from 3 camera positions (Cam 1, Cam 2, Cam 3)
- 📝 **Data Management**: Upload and store PPE detection images with metadata
- 📈 **Statistics Dashboard**: View total detections per camera
- 🖼️ **Image Storage**: Automatic image handling with UUID-based naming
- 🗄️ **MySQL Database**: Persistent data storage with structured schema

## Technology Stack

- **Backend**: Flask 3.1.1
- **Database**: MySQL
- **Authentication**: Flask-Login 0.6.3
- **Real-time Communication**: Flask-SocketIO 5.5.1
- **Frontend**: Bootstrap, jQuery, custom CSS/JS
- **Additional Libraries**: 
  - FlaskWebGUI (desktop application wrapper)
  - mysqlclient (MySQL connector)

## Prerequisites

- Python 3.13.x
- MySQL Server
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd Flask
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv313
   .venv313\Scripts\activate  # On Windows
   # or
   source .venv313/bin/activate  # On Linux/Mac
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

1. **Start MySQL server**

2. **Create the database**
   ```bash
   mysql -u root -p
   ```
   
   Then in MySQL shell:
   ```sql
   CREATE DATABASE ppe_detection;
   USE ppe_detection;
   ```

3. **Import database schema**
   ```sql
   source database/schema.sql;
   ```

4. **Seed initial data** (creates admin user)
   ```sql
   source database/seed.sql;
   ```

## Configuration

Update MySQL configuration in `app.py` if needed:

```python
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""  # Update with your password
app.config["MYSQL_DB"] = "ppe_detection"
```

## Running the Application

1. **Start the Flask application**
   ```bash
   python app.py
   ```

2. **Access the application**
   - Open your browser and navigate to: `http://localhost:5000`
   - Login credentials (default):
     - Username: `admin`
     - Password: `password123`

## Project Structure

```
Flask/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── setup.txt              # Setup instructions
├── database/
│   ├── schema.sql         # Database schema
│   ├── seed.sql           # Initial data
│   ├── reset.sql          # Reset database script
│   └── setupdatabase.txt  # Database setup guide
├── static/
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   ├── fonts/             # Font files
│   ├── images/            # Uploaded detection images
│   └── img/               # Static images
├── templates/
│   ├── home.html          # Dashboard page
│   ├── login.html         # Login page
│   └── form.html          # Upload form page
└── REQUIREMENTS/          # Additional requirements
```

## Database Schema

### Users Table
- `id`: Primary key (Auto-increment)
- `username`: Unique username (VARCHAR 50)
- `password`: User password (VARCHAR 100)

### PPE Detection Table
- `id`: Primary key (Auto-increment)
- `image`: Image filename (VARCHAR 255)
- `time`: Detection timestamp (Auto-generated)
- `classes`: PPE class/type (VARCHAR 50)
- `position`: Camera position (ENUM: 'Cam 1', 'Cam 2', 'Cam 3')

## Usage

### Login
1. Navigate to the login page
2. Enter credentials
3. Access the dashboard

### View Dashboard
- See all PPE detection records
- View statistics per camera
- Real-time updates when new data is added

### Upload Detection Data
1. Click on the form/upload option
2. Select an image
3. Choose PPE class
4. Select camera position
5. Submit the form

## API Endpoints

- `GET /login` - Login page
- `POST /login` - Authenticate user
- `GET /logout` - Logout user
- `GET /` - Dashboard (requires authentication)
- `GET /form` - Upload form (requires authentication)
- `POST /formpost` - Submit detection data

## Security Notes

⚠️ **Important**: This is a development version. For production:
- Change the default admin password
- Use environment variables for sensitive data
- Implement password hashing (bcrypt/argon2)
- Use HTTPS
- Update SECRET_KEY to a secure random value
- Implement CSRF protection
- Add input validation and sanitization

## Database Management

**Reset Database** (Warning: Deletes all data):
```sql
source database/reset.sql;
source database/schema.sql;
source database/seed.sql;
```

## Troubleshooting

- **MySQL Connection Error**: Ensure MySQL server is running and credentials are correct
- **Import Error**: Make sure all packages from requirements.txt are installed
- **Port Already in Use**: Change the port in app.py or kill the process using port 5000

## Future Enhancements

- Password hashing implementation
- User management (add/edit/delete users)
- Advanced filtering and search
- Export data to CSV/PDF
- Video stream integration
- AI model integration for automated PPE detection
- Role-based access control

## License

[Add your license here]

## Contributors

[Add contributors here]

## Support

For issues and questions, please open an issue on GitHub.
