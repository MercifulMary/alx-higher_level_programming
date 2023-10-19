-- Lists all shows in the hbtn_0d_tvshows database without a genre linked
-- This query retrieves the title of TV shows and their associated genre IDs from the tv_shows and tv_show_genres tables, listing only those shows that do not have a genre linked. The results are ordered by show title and genre ID in ascending order.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
