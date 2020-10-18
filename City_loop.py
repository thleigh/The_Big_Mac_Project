from Major_cities import major_cities
from Doordash import doordash, newDriver

def cities():
    for cities in major_cities[40:50]:
        # doordashDriver()
        doordash(cities)
        # newDriver()

cities()