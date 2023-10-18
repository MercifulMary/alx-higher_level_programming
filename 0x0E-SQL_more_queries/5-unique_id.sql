-- Creates the table unique_id on your MySQL server
-- This table has a default value of 1 for the 'id' column and enforces uniqueness
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
