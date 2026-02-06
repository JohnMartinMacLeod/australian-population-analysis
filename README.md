# Australian Population by Age (1971 - 2025)

## Overview

This project transforms raw population data (provided by the Australian Bureau of Statistics) into a clean, queryable PostgreSQL table.

The raw data was provided in a wide, Excel format and required significant resturctring before analysis.

## Pipeline

1. Raw XLSX files converted to CSV
2. Python (pandas) used to:
    - remove metadata rows
    - reshape wide to long format
    - extract sex and age dimensions
    - clean year and age values
3. Clean dataset saved as CSV
4. Data loaded into PostgreSQL
5. Analysis performed using SQL

## Final Table Schema

population_by_age:

- year (INTEGER)
- sex (TEXT)
- age (INTEGER)
- population (INTEGER)

## Example Questions Answered

- How has the total population of Australia changed over time?
- What does the population pyramid look like of a given year?
- How has the 65+ population grown since 1971?

## Tools Used

- Python
- Pandas library
- PostgreSQL
- DBeaver
