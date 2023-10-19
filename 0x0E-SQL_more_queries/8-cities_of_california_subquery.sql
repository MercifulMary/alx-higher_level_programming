-- Lists all the cities of California found in the database hbtn_0d_usa
-- This query retrieves the id and name of cities located in the state of California and orders them by id in ascending order.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
