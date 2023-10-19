-- Lists all genres from the hbtn_0d_tvshows database not linked to the show 'Dexter'
-- This query retrieves the names of genres that are not linked to the TV show 'Dexter' by comparing the names in the tv_genres table with the genres linked to 'Dexter' in the tv_show_genres and tv_shows tables. The results are ordered alphabetically by genre name.
SELECT name
FROM tv_genres
WHERE name NOT IN
(SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter')
GROUP BY name
ORDER BY name ASC;
