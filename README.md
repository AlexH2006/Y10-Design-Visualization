# Y10-Design-Visualization
This project, visualizes the secondary enrollment in different countries with different incomes since 1970 to 2020 as a growing tree.

# Raw Data:
1. API_SE.SEC.ENRR_DS2_en_csv_v2_4672725.csv: Secondary School Enrollment Rate(%), by country by year, from 1960 to 2021. (UNESCO Institute for Statistics, 2022)
2. API_SP.POP.0014.TO_DS2_en_csv_v2_4661114.csv: Population Ages 0~14 (%), by country by year, from 1960 to 2021 (The World Bank, 2019)
3. Countries-Continents.csv: Classification of Country by Continents (World Population Review, 2022)
4. Metadata_Country_API_SE.SEC.ENRR_DS2_en_csv_v2_4672725.csv: Classification of Country by Income (UNESCO Institute for Statistics, 2022)
5. Metadata_Country_API_SP.POP.0014.TO_DS2_en_csv_v2_4661114.csv: Same as 5
6. gdp-per-capita-maddison-2020.csv: Gdp per capita by country by year (World Bank, 2022)

Note: File 5 and File 3 are not used in the code, but they are crucial to future improvements.

# Code:
There are two different versions of codes (Tree_Income.py and Tree_Income_population.py). However, the key ideas are the same.

1. Each dot represents 3,000,000 students go to a secondary school
2. The number of students enrolled in secondary school is only an estimation, because in the exact data, data from many years are missing. The calculation assumes the population aged 0-14 is relatively even distributed. Based on the population aged 0~14 in each country, we times 6/14 to get the secondary education population, as in avergae the secondary school is 6 years long.
3. Each white margin repsentes a decade. The inner-most ring represents data from 1970 to 1980.
4. The color of the dot represents the country income suggested in the legend.

Difference between two versions:
In Tree_Income.py, the mean value for random_angle is fixed in Guassian Random Numbers.
In Tree_Income_population.py, the differce between adjacent mean value for random_angle is calculated proportional to the number of dots being dropped, which makes it more visually appealing.

# References:
1. Cruz, P., Wihbey, J., Ghael, A., Costa, S., Chao, R., & Shibuya, F. (n.d.). VISAP’18, Annotated portfolios and annotated projects. Retrieved December 20, 2022, from https://web.northeastern.edu/naturalizing-immigration-dataviz/download/portfolio-camera-ready.pdf
2. The World Bank. (2019). Population ages 0-14 (% of total population) | Data. Worldbank.org. https://data.worldbank.org/indicator/SP.POP.0014.TO.ZS
3. UNESCO Institute for Statistics. (2022, June). School enrollment, secondary (% gross) | Data. Data.worldbank.org. https://data.worldbank.org/indicator/SE.SEC.ENRR?end=2021&most_recent_year_desc=true&start=1970
4. World Bank. (2022). GDP per capita (current US$) | Data. Worldbank.org. https://data.worldbank.org/indicator/NY.GDP.PCAP.CD
5. World Population Review. (2022). List Of Countries By Continent 2021. Worldpopulationreview.com. https://worldpopulationreview.com/country-rankings/list-of-countries-by-continent
