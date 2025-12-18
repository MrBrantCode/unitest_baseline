"""
QUESTION:
Create a function called `filter_european_countries` that takes a list of tuples containing European country names and their corresponding populations as input. The function should return a list of tuples containing the countries with a population greater than or equal to 5 million.
"""

def filter_european_countries(countries):
    """
    Filter out European countries with a population greater than or equal to 5 million.

    Args:
        countries (list): A list of tuples containing European country names and their corresponding populations.

    Returns:
        list: A list of tuples containing the countries with a population greater than or equal to 5 million.
    """
    return [(country, population) for (country, population) in countries if population >= 5000000]