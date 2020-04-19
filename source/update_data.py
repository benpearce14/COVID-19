import wget
import os

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

print('\n----------------------')
print('Data has been updated!')
print('----------------------')

