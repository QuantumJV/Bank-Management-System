CREATE DATABASE bank;

USE bank;


CREATE TABLE ACCOUNT (
    AccountNo BIGINT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Age INT,
    Occupation VARCHAR(255),
    Address VARCHAR(255),
    MobileNo BIGINT UNIQUE,
    AadharNumber BIGINT UNIQUE,
    Amount FLOAT,
    AccountType VARCHAR(50)
);


CREATE TABLE amount (
    TransactionID BIGINT AUTO_INCREMENT PRIMARY KEY,
    AccountNo BIGINT,
    AmountDeposite FLOAT,
    AmountWithdrawn FLOAT,
    Month VARCHAR(50),
    FOREIGN KEY (AccountNo) REFERENCES account(AccountNo)
);


CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (username, password) VALUES ('bank_admin', 'bank_password');
