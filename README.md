# MAT2007-Project

Analysis of OWID Energy dataset

**Filters:** Data was filtered to only contain countries (No regions, groups etc.), and to have years between 1985 and 2024.

**Packages:** pandas, numpy, matplotlib.pyplot

**Link to the github with the data and the codebook (meaning of each column):** https://github.com/owid/energy-data

**What does the script do?**

The script produces the following outputs:

Global energy consumption: Two pie charts showing the energy consumption of the 15 largest consuming countries and the combined consumption of all other countries in 1985 and 2024. The total global consumption is also displayed.

Global energy mix: A line graph showing the global shares of fossil, renewable and nuclear energy from 1985 to 2024.

Country energy mixes: Four line graphs showing the shares of fossil, renewable and nuclear energy for the United States, China, Russia and India over the same period.

Country-level changes: Three horizontal bar charts showing the change in fossil, renewable and nuclear energy shares, in percentage points, for each country between 1985 and 2024.

Numerical results: The script prints the percentage-point changes for each country, as well as the mean changes and standard deviations for the selected geographical regions and across all included countries.

**How to run the code?**

Make sure the packages are installed and open the code in a code editor, make sure the read function has the correct path to the Energy_data.csv file on your device. Select which functions you want to run and run the script using python.

## Questions

### 1. How has energy consumption changed globally between 1985 and 2024?

- 2 plots included: 1 'Pie' chart for 1985 of total consumption and one for 2024

### 2. How has the global energy mix changed between 1985 and 2024?

- 5 plots included: 1 for the renewable, nuclear and fossil shares over time globally, and 4 for each of the big 4 countries (USA, China, Russia, India).

### 3. How differently have countries transitioned their energy mixes between 1985 and 2024?

- 3 plots included: 1 for each catagory with the percentage point change of each country between 1985 and 2024

---

## How has energy consumption changed globally between 1985 and 2024?

- Global Consumption : +109.21%
- USA : +31.02%
- Russia: -5.40%
- China: +690.30% & 7.59% -> 28.68% of global share
- India: +615.93%

## How has the global energy mix changed between 1985 and 2024?

- Fossil: 88.21% -> 81.29% | Difference: -6.91 pp
- Renewable: 6.70% -> 14.65% | Difference: +7.94 pp
- Nuclear: 5.09% -> 4.06% | Difference: -1.03 pp

## How differently have countries transitioned their energy mixes between 1985 and 2024?

### Biggest increases in each catagory:

- Fossil: Taiwan 15.80 pp
- Renewable: Denmark 41.57 pp
- Nuclear: Czechia 17.51 pp

### Biggest decreases in each catagory:

- Fossil: Denmark -41.57 pp
- Renewable: Philippines -12.21 pp
- Nuclear: Taiwan -17.85 pp

### Mean change with std as uncertainty for regions:

**Global**
- Fossil: -8.83 ± 9.94 pp
- Renewable: 7.95 ± 8.88 pp
- Nuclear: 0.88 ± 5.24 pp

**Europe**
- Fossil: -17.53 ± 7.97 pp
- Renewable: 15.34 ± 7.99 pp
- Nuclear: 2.18 ± 7.15 pp

**North America**
- Fossil: -2.65 ± 6.65 pp
- Renewable: 1.72 ± 5.40 pp
- Nuclear: 0.93 ± 1.34 pp

**South America**
- Fossil: -5.60 ± 4.92 pp
- Renewable: 5.66 ± 4.82 pp
- Nuclear: -0.06 ± 0.31 pp

**East Asia**
- Fossil: -2.10 ± 11.69 pp
- Renewable: 5.27 ± 4.95 pp
- Nuclear: -3.17 ± 
