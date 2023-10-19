-- Lists all Comedy shows in the hbtn_0d_tvshows database
-- This query retrieves the titles of TV shows that belong to the 'Comedy' genre by joining the tv_shows, tv_show_genres, and tv_genres tables. The results are grouped by title and ordered alphabetically.
SELECT title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
GROUP BY title
ORDER BY title ASC;
