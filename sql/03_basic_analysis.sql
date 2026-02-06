-- Total population over 65 by year
SELECT
    year,
    SUM(population) AS population_over_65
FROM population_by_age
WHERE sex = 'Persons' AND age >= 65
GROUP BY year
ORDER BY year;