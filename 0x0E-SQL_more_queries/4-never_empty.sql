-- Creates the table id_not_null on your MySQL server
-- This table has a default value of 1 for the 'id' column
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
