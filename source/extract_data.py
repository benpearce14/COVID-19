import numpy as np
import pandas as pd


def extract_countries(country_list):
    '''Extract raw data for given list of countries'''

    data_populations = pd.read_csv('../raw_data/populations.csv')
    data_confirmed = pd.read_csv('../raw_data/confirmed.csv')
    data_recovered = pd.read_csv('../raw_data/recovered.csv')
    data_deaths = pd.read_csv('../raw_data/deaths.csv')
    countries_info = []

    for i in range(len(country_list)):

        country_name = country_list[i]
        population = data_populations.loc[data_populations['Combined_Key'] == country_name]
        confirmed = data_confirmed.loc[data_confirmed['Country/Region'] == country_name]
        recovered = data_recovered.loc[data_recovered['Country/Region'] == country_name]
        deaths = data_deaths.loc[data_deaths['Country/Region'] == country_name]
        population = float(population.iloc[0,11])
        dates = confirmed.columns.values.tolist()[4:]

        if len(confirmed) > 1:
            if len(confirmed[confirmed['Province/State'].isnull()]) > 0:
                confirmed = confirmed[confirmed['Province/State'].isnull()]
                recovered = recovered[recovered['Province/State'].isnull()]
                deaths = deaths[deaths['Province/State'].isnull()]
                confirmed = confirmed.iloc[0,4:].values
                recovered = recovered.iloc[0,4:].values
                deaths = deaths.iloc[0,4:].values
            else:
                confirmed = confirmed.sum().tolist()[4:]
                recovered = recovered.sum().tolist()[4:]
                deaths = deaths.sum().tolist()[4:]
        else:
            confirmed = confirmed.iloc[0,4:].values
            recovered = recovered.iloc[0,4:].values
            deaths = deaths.iloc[0,4:].values

        countries_info.append([country_name, population, np.asarray(dates), np.asarray(confirmed), \
                               np.asarray(recovered), np.asarray(deaths)])

    return countries_info


if __name__ == '__main__':
    print("Run as test code")
    import plotting_routines as pr
    
    country_list = ['France', 'Germany', 'United Kingdom', 'China', 'US', \
                    'Korea, South', 'Italy', 'Spain']
    countries_info = extract_countries(country_list)
    
    pr.plot_countries(countries_info)
    pr.plot_countries_confirmed_million(countries_info)
    pr.plot_countries_recovered_million(countries_info)
    pr.plot_countries_deaths_million(countries_info)
    
    print("Test run completed")
