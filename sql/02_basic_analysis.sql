-- Male & Female population by age in 2025
SELECT
    age,
    SUM(CASE WHEN sex = 'Male' THEN population ELSE 0 END) AS male_population,
    SUM(CASE WHEN sex = 'Female' THEN population ELSE 0 END) AS female_population
FROM population_by_age
WHERE year = 2025
GROUP BY age
ORDER BY age;