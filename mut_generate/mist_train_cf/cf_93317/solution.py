"""
QUESTION:
Create a function called `get_num_cities(country)` that takes a country name as input and returns the number of cities in that country, with a time complexity of O(1). The function should have access to a dictionary where country names are keys and lists of cities are values. If the country name is not found in the dictionary, the function should return 0.
"""

def get_num_cities(country, countries):
    if country in countries:
        return len(countries[country])
    else:
        return 0