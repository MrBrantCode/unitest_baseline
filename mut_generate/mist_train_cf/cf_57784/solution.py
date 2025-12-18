"""
QUESTION:
Create a function called `find_densest_city` that takes a list of dictionaries representing cities, where each city has 'name', 'area', and 'population' keys, and returns the name of the city with the highest population density.
"""

def find_densest_city(cities):
    """
    This function takes a list of dictionaries representing cities and returns the name of the city with the highest population density.

    Args:
    cities (list): A list of dictionaries, where each dictionary contains 'name', 'area', and 'population' keys.

    Returns:
    str: The name of the city with the highest population density.
    """
    # Calculate population density for each city and add it to the dictionary
    for city in cities:
        city['population_density'] = city['population'] / city['area']

    # Sort the cities by population density in descending order
    cities.sort(key=lambda x: x['population_density'], reverse=True)

    # Return the city with the highest population density
    return cities[0]['name']