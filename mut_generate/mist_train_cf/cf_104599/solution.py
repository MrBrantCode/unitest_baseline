"""
QUESTION:
Write a function named `find_top_countries` that takes a list of dictionaries representing countries and their populations as input. The function should find and return the names and populations of the five most populous countries, the average population of these top five countries, and the name and population of the country with the lowest population. The function should use efficient algorithms to minimize unnecessary iterations and optimize data structure usage. The input list of countries is already given and does not need to be generated within the function.
"""

def find_top_countries(countries):
    """
    Find and return the names and populations of the five most populous countries, 
    the average population of these top five countries, and the name and population 
    of the country with the lowest population.

    Args:
        countries (list): A list of dictionaries representing countries and their populations.

    Returns:
        tuple: A tuple containing the names and populations of the top five countries, 
        the average population of these top five countries, and the name and population 
        of the country with the lowest population.
    """

    # Sort the countries based on their population in descending order
    countries.sort(key=lambda x: x['population'], reverse=True)

    # Extract the names and populations of the five most populous countries
    top_five_countries = [(country['name'], country['population']) for country in countries[:5]]

    # Calculate the average population of the top five countries
    average_population = sum(country['population'] for country in countries[:5]) / 5

    # Find the country with the lowest population
    lowest_population_country = min(countries, key=lambda x: x['population'])
    lowest_population = (lowest_population_country['name'], lowest_population_country['population'])

    return top_five_countries, average_population, lowest_population