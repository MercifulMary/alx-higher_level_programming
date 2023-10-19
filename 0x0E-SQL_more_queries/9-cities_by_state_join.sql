-- Lists all cities in the hbtn_0d_usa database
-- This query retrieves the id and name of cities and their corresponding states from the cities table, including cities without associated states. It then orders the results by city id.
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
