from Major_cities import major_cities
from Doordash import doordash, teardown, doordashDriver, newDriver

def cities():
    doordashDriver()
    for cities in major_cities[:10]:
        doordash(cities)
        teardown()
        newDriver()

cities()