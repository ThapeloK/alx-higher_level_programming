-- Script that lists all the cities of California that can be found in the database
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities ON states.id=cities.state_id
ORDER BY cities.id;
