from Major_cities import major_cities
from Doordash import doordash

def cities():
    for cities in major_cities[0:10]:
        doordash(cities)
    # doordash('Santa Monica')
cities()
