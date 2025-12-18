"""
QUESTION:
Construct a function named `get_population_dict` that takes a list of countries (which may contain duplicate values) and returns a dictionary with each country as a key and its total population (number of occurrences in the list) as the value. The dictionary should be sorted in descending order of population.
"""

def get_population_dict(countries):
    """Return a dictionary with each country as a key and its total population as the value.
    The dictionary is sorted in descending order of population."""
    
    # Create a dictionary to store countries and their population
    population_dict = {}
    
    # Iterate over the countries and update population values
    for country in countries:
        population_dict[country] = population_dict.get(country, 0) + 1
    
    # Sort the dictionary by population in descending order
    return dict(sorted(population_dict.items(), key=lambda x: x[1], reverse=True))