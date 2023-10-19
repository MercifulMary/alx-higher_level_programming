-- Lists all genres from the hbtn_0d_tvshows database and displays the number of shows linked to each genre
-- This query retrieves genre names from the tv_genres table and counts the number of shows linked to each genre from the tv_show_genres table. The results are grouped by genre and ordered by the number of shows in descending order.
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
