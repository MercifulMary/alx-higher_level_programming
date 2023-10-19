-- Lists all TV genres from the hbtn_0d_tvshows_rate database by their total rating
-- This query retrieves genre names and calculates their total ratings by joining the tv_genres, tv_show_genres, and tv_show_ratings tables. The results are then grouped by genre name and ordered by rating in descending order.
SELECT name, SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;
