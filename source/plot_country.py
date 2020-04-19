import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import sys


def extract_countries(country_list):
    '''Extract raw data for given list of countries'''
    data_populations = pd.read_csv('../data/populations.csv')
    data_confirmed = pd.read_csv('../data/confirmed.csv')
    data_recovered = pd.read_csv('../data/recovered.csv')
    data_deaths = pd.read_csv('../data/deaths.csv')
    countries_info = []
    for i in range(len(country_list)):
        country_name = country_list[i]
        population = data_populations.loc[data_populations['Combined_Key'] == country_name]
        confirmed = data_confirmed.loc[data_confirmed['Country/Region'] == country_name]
        recovered = data_recovered.loc[data_recovered['Country/Region'] == country_name]
        deaths = data_deaths.loc[data_deaths['Country/Region'] == country_name]
        population = int(population.iloc[0,11])
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
    countries_info.append([country_name, population, dates, confirmed, recovered, deaths])
    return countries_info


def plot_countries(countries_info):
    '''Plot raw data for given list of countries'''
    for i in range(len(countries_info)):
        dates = countries_info[i][2]
        x_vals = np.arange(0,len(dates))
        plt.figure()
        plt.plot(x_vals, countries_info[i][3], label='Confirmed')
        plt.plot(x_vals, countries_info[i][4], label='Recovered')
        plt.plot(x_vals, countries_info[i][5], label='Deaths')
        plt.title('%s' % countries_info[i][0])
        plt.xlim(0,max(x_vals))
        plt.xlabel('Days')
        plt.ylabel('N')
        plt.legend(loc=2)
        plt.semilogy()
        plt.savefig('%s.pdf' % countries_info[i][0])
        plt.close()
                   
    
if __name__ == '__main__':
    print("Run as test code")
    country_list = ["France", "Germany"]
    countries_info = extract_countries(country_list)
    print(countries_info)
    plot_countries(countries_info)
    print("Test run completed")
