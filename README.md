# MAT2007-Project
Analysis of OWID Energy dataset
Filters: Data was filtered to only contain countries (No regions, groups etc.), and to have years between 1985 and 2024.
Packages: pandas, numpy, matplotlib.pyplot
Link to the github with the data and the codebook (meaning of each column): https://github.com/owid/energy-data

Questions:
-How has energy consumption changed globally between 1985 and 2024? DONE!!!
    - 2 plots included: 1 'Pie' chart for 1985 of total consumption and one for 2024
-How has the global energy mix changed between 1985 and 2024? DONE!!!
    - 5 plots included: 1 for the renewable, nuclear and fossil shares over time globally, and 4 for each of the big 4 countries (USA, China, Russia, India).
-How differently have countries transitioned their energy mixes between 1985 and 2024? DONE!!!
    -3 plots included: 1 for each catagory with the percentage point change of each country between 1985 and 2024

How has energy consumption changed globally between 1985 and 2024?

Global Consumption : +109.21%
USA : +31.02%
Russia: -5.40%
China: +690.30% & 7.59% -> 28.68% of global share
India: +615.93%

How has the global energy mix changed between 1985 and 2024?

Fossil: 88.21% -> 81.29% | Difference: -6.91 pp
Renewable: 6.70% -> 14.65% | Difference: +7.94 pp   
Nuclear: 5.09% -> 4.06% | Difference: -1.03 pp

How differently have countries transitioned their energy mixes between 1985 and 2024?

Biggest increases in each catagory:
Fossil: Taiwan 15.80 pp
Renewable: Denmark 41.57 pp
Nuclear: Czechia 17.51 pp

Biggest decreases in each catagory:
Fossil: Denmark -41.57 pp 
Renewable: Philippines -12.21 pp
Nuclear: Taiwan -17.85 pp

Mean change with std as uncertainty for regions:
Global
    Fossil: -8.83 ± 9.94 pp
    Renewable: 7.95 ± 8.88 pp
    Nuclear: 0.88 ± 5.24 pp
Europe
    Fossil: -17.53 ± 7.97 pp
    Renewable: 15.34 ± 7.99 pp
    Nuclear: 2.18 ± 7.15 pp
North America
    Fossil: -2.65 ± 6.65 pp
    Renewable: 1.72 ± 5.40 pp
    Nuclear: 0.93 ± 1.34 pp
South America
    Fossil: -5.60 ± 4.92 pp
    Renewable: 5.66 ± 4.82 pp
    Nuclear: -0.06 ± 0.31 pp
East Asia
    Fossil: -2.10 ± 11.69 pp
    Renewable: 5.27 ± 4.95 pp
    Nuclear: -3.17 ± 9.12 pp
South Asia
    Fossil: 1.08 ± 2.42 pp
    Renewable: -2.63 ± 1.83 pp
    Nuclear: 1.55 ± 2.85 pp
Southeast Asia
    Fossil: -2.74 ± 9.12 pp
    Renewable: 2.74 ± 9.12 pp
    Nuclear: 0.00 ± 0.00 pp
Middle East
    Fossil: -2.54 ± 4.29 pp
    Renewable: 1.67 ± 3.46 pp
    Nuclear: 0.88 ± 2.29 pp
Central Asia
    Fossil: -1.85 ± 1.48 pp
    Renewable: 1.85 ± 1.48 pp
    Nuclear: 0.00 ± 0.00 pp
Africa
    Fossil: -1.83 ± 3.84 pp
    Renewable: 1.88 ± 3.87 pp
    Nuclear: -0.05 ± 0.11 pp

Full results:
Algeria: Fossil 0.44 pp | Renewable -0.44 pp | Nuclear 0.00 pp
Argentina: Fossil -2.11 pp | Renewable 2.82 pp | Nuclear -0.71 pp
Australia: Fossil -10.24 pp | Renewable 10.24 pp | Nuclear 0.00 pp
Austria: Fossil -14.84 pp | Renewable 14.84 pp | Nuclear 0.00 pp
Azerbaijan: Fossil -2.75 pp | Renewable 2.75 pp | Nuclear 0.00 pp
Bangladesh: Fossil 3.17 pp | Renewable -3.17 pp | Nuclear 0.00 pp
Belarus: Fossil -13.20 pp | Renewable 0.95 pp | Nuclear 12.24 pp
Belgium: Fossil -5.46 pp | Renewable 11.28 pp | Nuclear -5.82 pp
Brazil: Fossil -8.08 pp | Renewable 7.77 pp | Nuclear 0.30 pp
Bulgaria: Fossil -23.99 pp | Renewable 14.57 pp | Nuclear 9.41 pp
Canada: Fossil 3.72 pp | Renewable -3.16 pp | Nuclear -0.55 pp
Chile: Fossil -3.19 pp | Renewable 3.19 pp | Nuclear 0.00 pp
China: Fossil -15.56 pp | Renewable 13.29 pp | Nuclear 2.27 pp
Colombia: Fossil -2.01 pp | Renewable 2.01 pp | Nuclear 0.00 pp
Cyprus: Fossil -10.80 pp | Renewable 10.80 pp | Nuclear 0.00 pp
Czechia: Fossil -26.52 pp | Renewable 9.01 pp | Nuclear 17.51 pp
Denmark: Fossil -41.57 pp | Renewable 41.57 pp | Nuclear 0.00 pp
Ecuador: Fossil -10.27 pp | Renewable 10.27 pp | Nuclear 0.00 pp
Egypt: Fossil 1.99 pp | Renewable -1.99 pp | Nuclear 0.00 pp
Estonia: Fossil -17.95 pp | Renewable 17.95 pp | Nuclear 0.00 pp
Finland: Fossil -32.48 pp | Renewable 26.76 pp | Nuclear 5.72 pp
France: Fossil -20.42 pp | Renewable 9.06 pp | Nuclear 11.36 pp
Germany: Fossil -13.72 pp | Renewable 22.72 pp | Nuclear -9.00 pp
Greece: Fossil -17.52 pp | Renewable 17.52 pp | Nuclear 0.00 pp
Hong Kong: Fossil -1.05 pp | Renewable 1.05 pp | Nuclear 0.00 pp
Hungary: Fossil -22.28 pp | Renewable 12.58 pp | Nuclear 9.71 pp
Iceland: Fossil -20.34 pp | Renewable 20.34 pp | Nuclear 0.00 pp
India: Fossil -0.39 pp | Renewable 0.01 pp | Nuclear 0.39 pp
Indonesia: Fossil -9.09 pp | Renewable 9.09 pp | Nuclear 0.00 pp
Iran: Fossil 0.62 pp | Renewable -1.12 pp | Nuclear 0.50 pp
Iraq: Fossil 0.60 pp | Renewable -0.60 pp | Nuclear 0.00 pp
Ireland: Fossil -19.84 pp | Renewable 19.84 pp | Nuclear 0.00 pp
Israel: Fossil -9.79 pp | Renewable 9.79 pp | Nuclear 0.00 pp
Italy: Fossil -12.19 pp | Renewable 13.38 pp | Nuclear -1.20 pp
Japan: Fossil -1.04 pp | Renewable 6.64 pp | Nuclear -5.60 pp
Kazakhstan: Fossil -3.30 pp | Renewable 3.30 pp | Nuclear 0.00 pp
Kuwait: Fossil -0.08 pp | Renewable 0.08 pp | Nuclear 0.00 pp
Latvia: Fossil -21.85 pp | Renewable 21.85 pp | Nuclear 0.00 pp
Lithuania: Fossil -8.18 pp | Renewable 22.81 pp | Nuclear -14.62 pp
Luxembourg: Fossil -13.50 pp | Renewable 13.50 pp | Nuclear 0.00 pp
Malaysia: Fossil -2.18 pp | Renewable 2.18 pp | Nuclear 0.00 pp
Mexico: Fossil -2.11 pp | Renewable 0.81 pp | Nuclear 1.30 pp
Morocco: Fossil -6.60 pp | Renewable 6.60 pp | Nuclear 0.00 pp
Netherlands: Fossil -17.59 pp | Renewable 17.95 pp | Nuclear -0.37 pp
New Zealand: Fossil -2.19 pp | Renewable 2.19 pp | Nuclear 0.00 pp
Norway: Fossil -3.62 pp | Renewable 3.62 pp | Nuclear 0.00 pp
Oman: Fossil -1.12 pp | Renewable 1.12 pp | Nuclear 0.00 pp
Pakistan: Fossil -1.56 pp | Renewable -4.26 pp | Nuclear 5.81 pp
Peru: Fossil -0.30 pp | Renewable 0.30 pp | Nuclear 0.00 pp
Philippines: Fossil 12.21 pp | Renewable -12.21 pp | Nuclear 0.00 pp
Poland: Fossil -12.61 pp | Renewable 12.61 pp | Nuclear 0.00 pp
Portugal: Fossil -18.61 pp | Renewable 18.61 pp | Nuclear 0.00 pp
Qatar: Fossil -0.81 pp | Renewable 0.81 pp | Nuclear 0.00 pp
Romania: Fossil -21.73 pp | Renewable 14.16 pp | Nuclear 7.58 pp
Russia: Fossil -4.28 pp | Renewable 1.34 pp | Nuclear 2.94 pp
Saudi Arabia: Fossil -0.73 pp | Renewable 0.73 pp | Nuclear 0.00 pp
Singapore: Fossil -0.55 pp | Renewable 0.55 pp | Nuclear 0.00 pp
Slovakia: Fossil -22.74 pp | Renewable 8.83 pp | Nuclear 13.91 pp
South Africa: Fossil -3.15 pp | Renewable 3.37 pp | Nuclear -0.22 pp
South Korea: Fossil -8.64 pp | Renewable 3.33 pp | Nuclear 5.32 pp
Spain: Fossil -15.97 pp | Renewable 16.16 pp | Nuclear -0.18 pp
Sri Lanka: Fossil 3.09 pp | Renewable -3.09 pp | Nuclear 0.00 pp
Sweden: Fossil -18.08 pp | Renewable 21.28 pp | Nuclear -3.20 pp
Switzerland: Fossil -8.70 pp | Renewable 11.39 pp | Nuclear -2.69 pp
Taiwan: Fossil 15.80 pp | Renewable 2.04 pp | Nuclear -17.85 pp
Thailand: Fossil -2.00 pp | Renewable 2.00 pp | Nuclear 0.00 pp
Trinidad and Tobago: Fossil 0.08 pp | Renewable -0.08 pp | Nuclear 0.00 pp
Turkey: Fossil -11.07 pp | Renewable 11.07 pp | Nuclear 0.00 pp
Turkmenistan: Fossil -0.00 pp | Renewable 0.00 pp | Nuclear 0.00 pp
Ukraine: Fossil -23.59 pp | Renewable 7.23 pp | Nuclear 16.36 pp
United Arab Emirates: Fossil -9.05 pp | Renewable 2.52 pp | Nuclear 6.53 pp
United Kingdom: Fossil -18.89 pp | Renewable 20.83 pp | Nuclear -1.95 pp
United States: Fossil -9.56 pp | Renewable 7.52 pp | Nuclear 2.04 pp
Uzbekistan: Fossil -1.34 pp | Renewable 1.34 pp | Nuclear 0.00 pp
Venezuela: Fossil -13.25 pp | Renewable 13.25 pp | Nuclear 0.00 pp
Vietnam: Fossil -14.85 pp | Renewable 14.85 pp | Nuclear 0.00 pp
