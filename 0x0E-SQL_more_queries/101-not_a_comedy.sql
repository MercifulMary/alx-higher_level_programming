-- Lists all TV shows without the 'Comedy' genre in the hbtn_0d_tvshows database
-- This query retrieves the titles of TV shows that are not linked to the 'Comedy' genre by comparing the titles in the tv_shows table with the genres linked to 'Comedy' in the tv_show_genres and tv_genres tables. The results are ordered alphabetically by show title.
SELECT title
FROM tv_shows
WHERE title NOT IN
(SELECT title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy')
GROUP BY title
ORDER BY title ASC;
