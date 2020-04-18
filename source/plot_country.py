import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import sys

country_name = str(sys.argv[1])

data_populations = pd.read_csv('../data/populations.csv')
data_confirmed = pd.read_csv('../data/confirmed.csv')
data_recovered = pd.read_csv('../data/recovered.csv')
data_deaths = pd.read_csv('../data/deaths.csv')

country_population = data_populations.loc[data_populations['Combined_Key'] == country_name]
country_confirmed = data_confirmed.loc[data_confirmed['Country/Region'] == country_name]
country_recovered = data_recovered.loc[data_recovered['Country/Region'] == country_name]
country_deaths = data_deaths.loc[data_deaths['Country/Region'] == country_name]

country_population = int(country_population.iloc[0,11])
dates = country_confirmed.columns.values.tolist()[4:]

if len(country_confirmed) > 1:
    if len(country_confirmed[country_confirmed['Province/State'].isnull()]) > 0:
        country_confirmed = country_confirmed[country_confirmed['Province/State'].isnull()]
        country_recovered = country_recovered[country_recovered['Province/State'].isnull()]
        country_deaths = country_deaths[country_deaths['Province/State'].isnull()]
        country_confirmed = country_confirmed.iloc[0,4:].values
        country_recovered = country_recovered.iloc[0,4:].values
        country_deaths = country_deaths.iloc[0,4:].values
    else:
        country_confirmed = country_confirmed.sum().tolist()[4:]
        country_recovered = country_recovered.sum().tolist()[4:]
        country_deaths = country_deaths.sum().tolist()[4:]
else:
    country_confirmed = country_confirmed.iloc[0,4:].values
    country_recovered = country_recovered.iloc[0,4:].values
    country_deaths = country_deaths.iloc[0,4:].values

print(country_name)
print(country_population)
print(len(dates))
print(len(country_confirmed))
print(len(country_recovered))
print(len(country_deaths))

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
