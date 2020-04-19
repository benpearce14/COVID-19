import wget
import os
import pandas as pd

if not len(os.listdir('../data/') ) == 0:
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
confirmed_global = pd.read_csv('../raw_data/confirmed.csv', sep=',')
confirmed_us = pd.read_csv('../raw_data/confirmed.csv', sep=',')
all_confirmed.append(confirmed_global)
all_confirmed.append(confirmed_us)
merged_confirmed = pd.concat(all_confirmed, ignore_index=True, sort=True)
merged_confirmed.to_csv('../raw_data/confirmed.csv')

all_deaths = []
deaths_global = pd.read_csv('../raw_data/deaths.csv', sep=',')
deaths_us = pd.read_csv('../raw_data/deaths.csv', sep=',')
all_deaths.append(deaths_global)
all_deaths.append(deaths_us)
merged_deaths = pd.concat(all_deaths, ignore_index=True, sort=True)
merged_deaths.to_csv('../raw_data/deaths.csv')

print('\n----------------------')
print('Data has been updated!')
print('----------------------')

