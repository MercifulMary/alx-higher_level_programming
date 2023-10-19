-- Lists all TV shows from the hbtn_0d_tvshows_rate table by their average rating
-- This query retrieves the titles of TV shows and calculates their average ratings by joining the tv_shows and tv_show_ratings tables. The results are then grouped by show title and ordered by rating in descending order.
SELECT title, AVG(tv_show_ratings.rate) AS 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;
