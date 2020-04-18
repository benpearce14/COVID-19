import urllib.request

print('Beginning data update...')
url = 'https://pomber.github.io/covid19/timeseries.json'
urllib.request.urlretrieve(url, '../data/world.json')
print('Data has been updated')
