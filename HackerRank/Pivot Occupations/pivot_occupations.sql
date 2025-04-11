SELECT MAX(CASE WHEN Occupation ='Doctor' THEN name END) as Doctor,
  MAX(CASE WHEN Occupation ='Professor' THEN name END) as Professor,
  MAX(CASE WHEN Occupation ='Singer' THEN name END) as Singer,
  MAX(CASE WHEN Occupation ='Actor' THEN name END) as Actor
FROM (
    SELECT name, occupation, ROW_NUMBER() OVER(PARTITION BY Occupation ORDER BY name) as rn
    FROM Occupations
) as a
GROUP BY rn 
ORDER BY rn 
;
