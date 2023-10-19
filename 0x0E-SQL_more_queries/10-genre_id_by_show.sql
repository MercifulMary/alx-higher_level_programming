-- Lists all shows in the hbtn_0d_tvshows database with at least one linked genre
-- This query retrieves the title of TV shows and their associated genre IDs from the tv_shows and tv_show_genres tables, filtering only those shows with at least one linked genre. The results are ordered by show title and genre ID in ascending order.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
