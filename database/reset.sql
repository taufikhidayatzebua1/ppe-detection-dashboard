-- reset.sql

-- Hapus semua tabel jika ada
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS ppe_detection;


-- Buat ulang semua tabel
SOURCE C:/laragon/lokernow/database/schema.sql;

-- Isi data dummy (user dan job)
SOURCE C:/laragon/lokernow/database/seed.sql;