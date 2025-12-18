"""
QUESTION:
Create a function `calculate_country_population` that takes a dictionary of country-population pairs as input. The function should return the input dictionary and the average population of all countries in the dictionary. The input dictionary will contain country names as keys and their respective populations as values.
"""

def calculate_country_population(country_populations):
    """
    Calculate the average population of countries in the given dictionary.

    Args:
        country_populations (dict): A dictionary with country names as keys and their respective populations as values.

    Returns:
        dict: The input dictionary.
        float: The average population of all countries in the dictionary.
    """
    total_population = sum(country_populations.values())
    average_population = total_population / len(country_populations)
    return country_populations, average_population