CREATE DATABASE IF NOT EXISTS myhouse_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'myhouse_user'@'localhost' IDENTIFIED BY 'myhouse_password';
GRANT ALL PRIVILEGES ON myhouse_db.* TO 'myhouse_user'@'localhost';
FLUSH PRIVILEGES;
