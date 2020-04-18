import wget

print('Beginning data update...')
url = 'https://pomber.github.io/covid19/timeseries.json'
wget.download(url, '../data/world.json')
print('Data has been updated')
