"""
QUESTION:
Create a function named `calculate_average_population` that takes a dictionary of country-population pairs as input. The function should return a dictionary containing the country-population pairs and the average population of all countries. The average population must be calculated manually without using any built-in functions or libraries.
"""

def calculate_average_population(country_populations):
    """
    This function calculates the average population of countries given a dictionary of country-population pairs.

    Args:
        country_populations (dict): A dictionary containing country names as keys and their populations as values.

    Returns:
        dict: A dictionary containing the country-population pairs and the average population of all countries.
    """

    total_population = 0
    num_countries = 0

    # Calculate total population and number of countries
    for population in country_populations.values():
        total_population += population
        num_countries += 1

    # Calculate average population
    average_population = total_population // num_countries

    # Create a new dictionary with the country-population pairs and the average population
    result = country_populations.copy()
    result['average_population'] = average_population

    return result