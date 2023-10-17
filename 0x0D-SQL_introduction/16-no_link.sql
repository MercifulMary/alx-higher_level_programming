-- Lists all the records of the second_table having a name value in my MySQL server.
-- Records are ordered in descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
