-- Lists all shows and their linked genres from the hbtn_0d_tvshows database
-- This query retrieves the titles of TV shows and the names of genres linked to each show by joining the tv_shows, tv_show_genres, and tv_genres tables. The results are ordered alphabetically by show title and genre name.
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;
