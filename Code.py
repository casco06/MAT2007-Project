import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import packages

df = pd.read_csv(r'C:\Users\casco\OneDrive - Maastricht University\VS Code\MAT2007\Project\Energy_data.csv')
# read as dataframe

countries_85 = df[df['iso_code'].notna() & (pd.to_numeric(df['year']) >= 1985)]
# create a filter for just countries between 1985-2024

Total_cons_columns = [
    'biofuel_consumption', 'coal_consumption', 'gas_consumption',
    'hydro_consumption', 'nuclear_consumption', 'oil_consumption',
    'solar_consumption', 'wind_consumption', 'other_renewable_consumption',
] # create a list of  all the different consumptions

def pie_1985():

    total_cons_country_1985 = countries_85[countries_85['year'] == 1985].groupby('country')[Total_cons_columns].sum().sum(axis=1)
    total_cons_global_1985 = np.sum(total_cons_country_1985)
    # sum the totals for each country in 1985 and make a global aswell

    top_15_1985 = total_cons_country_1985.nlargest(15)
    other_1985 = total_cons_global_1985 - top_15_1985.sum()
    top_15_1985['Other'] = other_1985
    # make top 15 with other being the total consumption - that of the top 15

    top_15_1985.plot(kind = 'pie', labels = None, colormap = 'tab20')
    labels = [f'{country}: {value:.0f} TWh' for country, value in top_15_1985.items()]
    # make labels for the legend and use 20 unique colors

    plt.title('Global Energy Consumption 1985:\n'
    f'{int(total_cons_global_1985)} TWh')
    plt.legend(labels, title = 'Country', loc = 'upper left', bbox_to_anchor=(-0.05, 1), fontsize = '7')
    plt.tight_layout()
    plt.show()
    # adjust some labels, sizes, titles etc

def pie_2024():
    total_cons_country_2024 = countries_85[countries_85['year'] == 2024].groupby('country')[Total_cons_columns].sum().sum(axis=1)
    total_cons_global_2024 = np.sum(total_cons_country_2024)

    top_15_2024 = total_cons_country_2024.nlargest(15)
    other_2024 = total_cons_global_2024 - top_15_2024.sum()
    top_15_2024['Other'] = other_2024

    top_15_2024.plot(kind = 'pie', labels = None, colormap = 'tab20')
    labels = [f'{country}: {value:.0f} TWh' for country, value in top_15_2024.items()]
    plt.title('Global Energy Consumption 2024:\n'
    f'{int(total_cons_global_2024)} TWh')
    plt.legend(labels, title = 'Country', loc = 'upper left', bbox_to_anchor=(-0.05, 1), fontsize = '7')
    plt.tight_layout()
    plt.show()
    # do the same as in 1985 but switch numbers
# makes a circle diagram for 1985 and 2024 specifically with total consumption and country shares

fossil_columns = [
    'coal_consumption',
    'gas_consumption',
    'oil_consumption']

renewable_columns = [
    'biofuel_consumption',
    'hydro_consumption',
    'solar_consumption',
    'wind_consumption',
    'other_renewable_consumption']

nuclear_columns = [
    'nuclear_consumption']
# create catagories for each type of energy

def series_countries():

    years = range(1985, 2025)
    countries = ['Russia', 'China', 'United States', 'India']
    # make some parameters used in the loop

    for country in countries:

        fossil = []
        renewable = []
        nuclear = []
        # make empty lists for storing results

        for i in years:
            data = countries_85[
                (countries_85['year'] == i) &
                (countries_85['country'] == country)
            ]

            total = data[Total_cons_columns].sum().sum()
            fossil_total = data[fossil_columns].sum().sum()
            renewable_total = data[renewable_columns].sum().sum()
            nuclear_total = data[nuclear_columns].sum().sum()

            fossil.append(fossil_total / total * 100)
            renewable.append(renewable_total / total * 100)
            nuclear.append(nuclear_total / total * 100)
            # getting the data for each quantitity

        plt.figure()

        plt.plot(years, fossil, '-o', ms=3, label='Fossil Energy Share (%)')
        plt.plot(years, renewable, '-o', ms=3, label='Renewable Energy Share (%)')
        plt.plot(years, nuclear, '-o', ms=3, label='Nuclear Energy Share (%)')

        plt.xlabel('Year')
        plt.ylabel('Percentage of total energy consumption (%)')
        plt.title(f'{country}: Energy Consumption by Type')
        plt.legend()
        plt.ylim(0, 100)
        plt.show()
        # adjusting, resizing, coloring, blah blah

def series_global():
    years = range(1985, 2025)

    glob_tot = []
    glob_tot_ren = []
    glob_tot_fos = []
    glob_tot_nuc = []

    for i in years:
        total_cons_country_fossil = countries_85[countries_85['year'] == i].groupby('country')[fossil_columns].sum().sum(axis=1)
        total_cons_country_renewable = countries_85[countries_85['year'] == i].groupby('country')[renewable_columns].sum().sum(axis=1)
        total_cons_country_nuclear = countries_85[countries_85['year'] == i].groupby('country')[nuclear_columns].sum().sum(axis=1)
        total_cons_country = countries_85[countries_85['year'] == i].groupby('country')[Total_cons_columns].sum().sum(axis=1)

        global_total_cons = np.sum(total_cons_country)
        global_total_cons_renewable = np.sum(total_cons_country_renewable)
        global_total_cons_fossil = np.sum(total_cons_country_fossil)
        global_total_cons_nuclear = np.sum(total_cons_country_nuclear)

        glob_tot.append(global_total_cons)
        glob_tot_fos.append(global_total_cons_fossil / global_total_cons * 100)
        glob_tot_nuc.append(global_total_cons_nuclear / global_total_cons * 100)
        glob_tot_ren.append(global_total_cons_renewable / global_total_cons * 100)

    plt.plot(years, glob_tot_fos, label='Fossil Energy Share (%)', marker = 'o', ms=3)
    plt.plot(years, glob_tot_ren, label='Renewable Energy Share (%)', marker = 'o', ms=3)
    plt.plot(years, glob_tot_nuc, label='Nuclear Energy Share (%)', marker = 'o', ms=3)
    

    plt.title('Distribution of Global Energy Consumption')
    plt.xlabel('Year')
    plt.ylabel('Percentage of total energy consumption (%)')
    plt.legend()
    plt.show()
# creates graphs for shares of types of energy

def diff_85_24():

    countrieslist = []
    fossildiff = []
    rendiff = []
    nucdiff = []

    for country in countries_85['country'].unique():

        Tot_fos_85 = countries_85[(countries_85['country'] == country) & (countries_85['year'] == 1985)][fossil_columns].sum().sum()
        Tot_ren_85 = countries_85[(countries_85['country'] == country) & (countries_85['year'] == 1985)][renewable_columns].sum().sum()
        Tot_nuc_85 = countries_85[(countries_85['country'] == country) & (countries_85['year'] == 1985)][nuclear_columns].sum().sum()
        Tot_85 = countries_85[(countries_85['country'] == country) & (countries_85['year'] == 1985)][Total_cons_columns].sum().sum()

        Tot_fos_24 = countries_85[(countries_85['country'] == country) & (countries_85['year'] == 2024)][fossil_columns].sum().sum()
        Tot_ren_24 = countries_85[(countries_85['country'] == country) & (countries_85['year'] == 2024)][renewable_columns].sum().sum()
        Tot_nuc_24 = countries_85[(countries_85['country'] == country) & (countries_85['year'] == 2024)][nuclear_columns].sum().sum()
        Tot_24 = countries_85[(countries_85['country'] == country) & (countries_85['year'] == 2024)][Total_cons_columns].sum().sum()

        if Tot_85 == 0 or Tot_24 == 0:
            continue

        fos_share_85 = (Tot_fos_85/Tot_85) * 100
        ren_share_85 = (Tot_ren_85/Tot_85) * 100
        nuc_share_85 = (Tot_nuc_85/Tot_85) * 100

        fos_share_24 = (Tot_fos_24/Tot_24) * 100
        ren_share_24 = (Tot_ren_24/Tot_24) * 100
        nuc_share_24 = (Tot_nuc_24/Tot_24) * 100

        diff_fos = fos_share_24 - fos_share_85
        diff_ren = ren_share_24 - ren_share_85
        diff_nuc = nuc_share_24 - nuc_share_85

        countrieslist.append(country)
        fossildiff.append(diff_fos)
        rendiff.append(diff_ren)
        nucdiff.append(diff_nuc)

    def plotdiff(list, x_label):
        order = np.argsort(list)
        plt.figure(figsize=(10, 18))
        plt.barh(np.array(countrieslist)[order], np.array(list)[order])
        plt.title('Energy Share change 1985-2024 per country')
        plt.tick_params(axis='y', labelsize=7)
        plt.xlabel(x_label)
        plt.show()

    plotdiff(fossildiff, 'Change in Fossil fuel consumption (% points)')
    plotdiff(rendiff, 'Change in Renewable fuel consumption (% points)')
    plotdiff(nucdiff, 'Change in Nuclear fuel consumption (% points)')
    
    energy_changes = {country: (fossil, renewable, nuclear) for country, fossil, renewable, nuclear in zip(countrieslist, fossildiff, rendiff, nucdiff)}
    
    #for country, (fossil, renewable, nuclear) in energy_changes.items():
        #print(f"{country}: Fossil {fossil:.2f} pp | Renewable {renewable:.2f} pp | Nuclear {nuclear:.2f} pp")

    Europe = [
    'Austria', 'Belarus', 'Belgium', 'Bulgaria', 'Czechia', 'Denmark',
    'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary',
    'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg',
    'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia',
    'Slovakia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine',
    'United Kingdom']

    North_America = [
    'Canada', 'Mexico', 'United States' ]

    South_America = [
    'Argentina', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Peru', 'Venezuela']

    Central_America_Caribbean = [
    'Trinidad and Tobago']

    East_Asia = [
    'China', 'Hong Kong', 'Japan', 'South Korea', 'Taiwan']

    South_Asia = [
    'Bangladesh', 'India', 'Pakistan', 'Sri Lanka']

    Southeast_Asia = [
    'Indonesia', 'Malaysia', 'Philippines', 'Singapore', 'Thailand', 'Vietnam']

    Middle_East = [
    'Iran', 'Iraq', 'Israel', 'Kuwait', 'Oman', 'Qatar',
    'Saudi Arabia', 'United Arab Emirates']

    Central_Asia = [
    'Azerbaijan', 'Kazakhstan', 'Turkmenistan', 'Uzbekistan']

    Africa = [
    'Algeria', 'Egypt', 'Morocco', 'South Africa']
    
    regions = {
    'Europe': Europe,
    'North America': North_America,
    'South America': South_America,
    'Central America & Caribbean': Central_America_Caribbean,
    'East Asia': East_Asia,
    'South Asia': South_Asia,
    'Southeast Asia': Southeast_Asia,
    'Middle East': Middle_East,
    'Central Asia': Central_Asia,
    'Africa': Africa}

    for region, countries in regions.items():

        fossil = [energy_changes[country][0] for country in countries]
        renewable = [energy_changes[country][1] for country in countries]
        nuclear = [energy_changes[country][2] for country in countries]

        print(f"{region}")
        print(f"Fossil: {np.mean(fossil):.2f} ± {np.std(fossil, ddof=1):.2f} pp")
        print(f"Renewable: {np.mean(renewable):.2f} ± {np.std(renewable, ddof=1):.2f} pp")
        print(f"Nuclear: {np.mean(nuclear):.2f} ± {np.std(nuclear, ddof=1):.2f} pp")

    #print(np.mean(fossildiff), np.mean(rendiff), np.mean(nucdiff))
    #print(np.std(fossildiff), np.std(rendiff), np.std(nucdiff))
