DROP DATABASE IF EXISTS apptestai;
CREATE DATABASE apptestai character set utf8mb4 collate utf8mb4_general_ci;
USE apptestai;

-- users Table Create SQL
CREATE TABLE users
(
    `id`      INT         NOT NULL AUTO_INCREMENT, 
    `account` VARCHAR(64) NOT NULL UNIQUE,
    PRIMARY KEY (id)
);

-- user_details Table Create SQL
CREATE TABLE user_details
(
    `id`       INT          NOT NULL  AUTO_INCREMENT,
    `user_id`  INT          NOT NULL,
    `name`     VARCHAR(45)  NOT NULL,
    `birthday` DATE         NOT NULL,
    `memo`     VARCHAR(512) NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id)
    REFERENCES users(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);
