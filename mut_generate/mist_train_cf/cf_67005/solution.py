"""
QUESTION:
Create a function named `country_info` that takes a list of dictionaries as input, where each dictionary contains information about a country, including 'name', 'population', and 'GDP'. The function should return the country with the highest population and the list of countries sorted by GDP per capita in descending order.
"""

from operator import itemgetter

def country_info(countries):
    """
    This function takes a list of dictionaries as input, where each dictionary contains 
    information about a country, including 'name', 'population', and 'GDP'. 
    The function returns the country with the highest population and the list of 
    countries sorted by GDP per capita in descending order.

    Args:
        countries (list): A list of dictionaries containing country information.

    Returns:
        tuple: A tuple containing the country with the highest population and 
        the list of countries sorted by GDP per capita in descending order.
    """

    # Find the country with the highest population
    highest_population_country = max(countries, key=itemgetter('population'))

    # Calculate GDP per capita for each country
    for country in countries:
        country['GDP per capita'] = country['GDP'] / country['population']

    # Sort the list by GDP per capita in descending order
    countries.sort(key=itemgetter('GDP per capita'), reverse=True)

    return highest_population_country, countries