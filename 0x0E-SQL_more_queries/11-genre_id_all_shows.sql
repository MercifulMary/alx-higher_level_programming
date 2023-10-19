-- Lists all shows in the hbtn_0d_tvshows database
-- This query retrieves the title of TV shows and their associated genre IDs from the tv_shows and tv_show_genres tables, listing all shows contained in the database. The results are ordered by show title and genre ID in ascending order.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
