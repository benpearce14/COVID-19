import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import sys

country_list = ["France", "Germany"]

def extract_country(country_list):

    data_populations = pd.read_csv('../data/populations.csv')
    data_confirmed = pd.read_csv('../data/confirmed.csv')
    data_recovered = pd.read_csv('../data/recovered.csv')
    data_deaths = pd.read_csv('../data/deaths.csv')
    countries_info = []

    for i in range(len(country_list)):
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
    
    countries_info.append([country_name, population, confirmed, recovered, deaths])
    return countries_info
        
'''print(country_name)
print(country_population)
print(len(dates))
print(len(country_confirmed))
print(len(country_recovered))
print(len(country_deaths))'''

print(countries_info)

x_vals = np.arange(0,len(dates))
plt.figure()
plt.plot(x_vals, country_confirmed, label='Confirmed')
plt.plot(x_vals, country_recovered, label='Recovered')
plt.plot(x_vals, country_deaths, label='Deaths')
plt.title('%s' % country_name)
plt.xlim(0,max(x_vals))
plt.xlabel('Days')
plt.ylabel('N')
plt.legend(loc=2)
plt.semilogy()
plt.savefig('%s.pdf' % country_name)
