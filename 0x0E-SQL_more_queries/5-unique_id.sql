-- Script that creates the table force_name on MySQL server
-- Create table unique_id
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
