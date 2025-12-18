"""
QUESTION:
Write a function `city_with_highest_population_density` that takes a list of dictionaries representing cities, where each dictionary contains the city's name, area, and population. The function should return the name of the city with the highest population density. The population density is calculated as the population divided by the area.
"""

def city_with_highest_population_density(cities):
    """
    Returns the name of the city with the highest population density.

    Args:
        cities (list): A list of dictionaries representing cities, where each dictionary contains the city's name, area, and population.

    Returns:
        str: The name of the city with the highest population density.
    """
    max_density = 0
    city_max_density = ""

    for city in cities:
        population_density = city['population'] / city['area']
        if population_density > max_density:
            max_density = population_density
            city_max_density = city['name']

    return city_max_density