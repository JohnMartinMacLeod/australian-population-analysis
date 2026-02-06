-- Total population by year
SELECT
    year,
    SUM(population) AS total_population
FROM population_by_age
WHERE sex = 'Persons'
GROUP BY year
ORDER BY year;