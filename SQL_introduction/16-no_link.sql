-- lists score and name of records with a name, ordered by score (top first)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;