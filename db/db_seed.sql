CREATE DATABASE mydb;
USE mydb;

CREATE USER 'flaskdbuser'@'%' IDENTIFIED BY 'Pa$$w0rd';
IDENTIFIED WITH caching_sha2_password BY 'Pa$$w0rd';
GRANT ALL on *.* to 'flaskdbuser'@'%' ;

FLUSH PRIVILEGES;

CREATE TABLE mytable( 
    id INT NOT NULL AUTO_INCREMENT,
    message VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)
);
INSERT INTO mytable(message) VALUES 
    ('Hello World!'),
    ('foo'),
    ('bar')
;
