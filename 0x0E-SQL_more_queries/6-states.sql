-- Creates database and table
-- Create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use hbtn_0d_usa
USE hbtn_0d_usa;
-- usage of primary key
CREATE TABLE IF NOT EXISTS states(id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id));
