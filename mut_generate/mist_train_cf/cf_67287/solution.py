"""
QUESTION:
Create a function `list_to_dict` that transforms a list of lists into a nested dictionary representation. Each sublist should contain a territory's name, population, GDP per capita, and annual deaths due to natural calamities. The function should return a dictionary where each key is a territory's name and its corresponding value is another dictionary with keys "Population", "GDP per Capita", and "Annual Deaths Due to Natural Calamities".

Implement another function `calc_percentage_of_world_population` that takes a territory's name and the current worldwide population as input and returns the territory's population as a percentage of the world population. The function should retrieve population data from the dictionary created by `list_to_dict`. The result should be rounded to two decimal places.
"""

def list_to_dict(lst):
    """Transforms a list of lists into a nested dictionary representation."""
    dict_ = dict()
    for arr in lst:
        dict_[arr[0]] = {
            "Population": arr[1],
            "GDP per Capita": arr[2],
            "Annual Deaths Due to Natural Calamities": arr[3]
        }
    return dict_

def calc_percentage_of_world_population(data, country, world_pop):
    """Calculates a territory's population as a percentage of the world population."""
    country_population = data[country]['Population']
    percentage_population = (country_population / world_pop) * 100
    return round(percentage_population, 2)