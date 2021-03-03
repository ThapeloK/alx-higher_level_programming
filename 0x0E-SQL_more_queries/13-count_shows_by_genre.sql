-- Script that lists all the cities of California that can be found in the database
SELECT tv_genres.name genre, COUNT(tv_show_genres.genre_id) number_of_shows
FROM tv_show_genres
LEFT JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
