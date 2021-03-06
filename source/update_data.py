import wget
import os
import pandas as pd

if not len(os.listdir('../raw_data/') ) == 0:
    os.system('rm ../raw_data/*.csv')

print('------------------------')
print('Beginning data update...')
print('------------------------')

url='https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/'
wget.download('%s/UID_ISO_FIPS_LookUp_Table.csv' % url, '../raw_data/populations.csv')
wget.download('%s/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv' % url, '../raw_data/confirmed.csv')
wget.download('%s/csse_covid_19_time_series/time_series_covid19_recovered_global.csv' % url, '../raw_data/recovered.csv')
wget.download('%s/csse_covid_19_time_series/time_series_covid19_deaths_global.csv' % url, '../raw_data/deaths.csv')

wget.download('%s/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv' % url, '../raw_data/confirmed_us.csv')
wget.download('%s/csse_covid_19_time_series/time_series_covid19_deaths_US.csv' % url, '../raw_data/deaths_us.csv')

all_confirmed = []
confirmed_global = pd.read_csv('../raw_data/confirmed.csv')
confirmed_us = pd.read_csv('../raw_data/confirmed_us.csv')
confirmed_us.rename(columns = {'Country_Region':'Country/Region'}, inplace = True) 
confirmed_us.rename(columns = {'Province_State':'Province/State'}, inplace = True) 
confirmed_us.rename(columns = {'Long_':'Long'}, inplace = True) 
confirmed_us = confirmed_us.filter(confirmed_global.columns.tolist())
all_confirmed.append(confirmed_global)
all_confirmed.append(confirmed_us)
merged_confirmed = pd.concat(all_confirmed, sort=False)
merged_confirmed.to_csv('../raw_data/confirmed.csv', index=False)

all_deaths = []
deaths_global = pd.read_csv('../raw_data/deaths.csv')
deaths_us = pd.read_csv('../raw_data/deaths_us.csv')
deaths_us.rename(columns = {'Country_Region':'Country/Region'}, inplace = True) 
deaths_us.rename(columns = {'Province_State':'Province/State'}, inplace = True) 
deaths_us.rename(columns = {'Long_':'Long'}, inplace = True) 
deaths_us = deaths_us.filter(deaths_global.columns.tolist())
all_deaths.append(deaths_global)
all_deaths.append(deaths_us)
merged_deaths = pd.concat(all_deaths, sort=False)
merged_deaths.to_csv('../raw_data/deaths.csv', index=False)

print('\n----------------------')
print('Data has been updated!')
print('----------------------')

