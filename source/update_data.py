import wget
import os

data_path='../data/world.json'

if os.path.exists(data_path):
    os.system('rm %s' % data_path)

print('Beginning data update...')
url = 'https://pomber.github.io/covid19/timeseries.json'
wget.download(url, '../data/world.json')
print('\nData has been updated')
