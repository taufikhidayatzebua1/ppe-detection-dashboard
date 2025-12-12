CREATE TABLE `users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
);

CREATE TABLE `ppe_detection` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `image` VARCHAR(255) NOT NULL,
  `time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `classes` VARCHAR(50) NOT NULL,
  `position` ENUM('Cam 1', 'Cam 2', 'Cam 3') NOT NULL,
  PRIMARY KEY (`id`)
);