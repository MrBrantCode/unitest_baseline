"""
QUESTION:
Create a function `construct_population_dict` that takes a list of countries with duplicate values as input, constructs a dictionary where the keys are the countries and the values are the number of occurrences of each country in the list (i.e., their total population), and returns the dictionary sorted in descending order of population.
"""

def construct_population_dict(countries):
    """
    Construct a dictionary where keys are countries and values are the number of occurrences of each country in the list.
    
    Args:
    countries (list): A list of countries with duplicate values.
    
    Returns:
    dict: A dictionary sorted in descending order of population.
    """
    # Create a dictionary to store countries and their population
    population_dict = {}
    
    # Iterate over the countries and update population values
    for country in countries:
        population_dict[country] = population_dict.get(country, 0) + 1
    
    # Sort the dictionary by population in descending order
    return dict(sorted(population_dict.items(), key=lambda x: x[1], reverse=True))