"""
QUESTION:
Calculate the weighted rank of cities based on their population sizes and GDP per capita. The weighted rank should be calculated using the formula: (0.6 * population rank) + (0.4 * GDP per capita rank), where population rank and GDP per capita rank are calculated by ranking the cities based on their population sizes and GDP per capita, respectively. The function should take a dictionary of cities with their population sizes and GDP per capita as input and return a dictionary with the weighted ranks of the cities.
"""

def calculate_weighted_rank(data):
    """
    Calculate the weighted rank of cities based on their population sizes and GDP per capita.

    Args:
        data (dict): A dictionary of cities with their population sizes and GDP per capita.

    Returns:
        dict: A dictionary with the weighted ranks of the cities.
    """

    # Calculate population rank
    population_rank = sorted(data.items(), key=lambda x: x[1]['population'], reverse=True)

    # Calculate GDP per capita rank
    gdp_rank = sorted(data.items(), key=lambda x: x[1]['gdp_per_capita'], reverse=True)

    # Calculate weighted rank
    weighted_rank = {}
    for city in data:
        population_index = next(i for i, x in enumerate(population_rank) if x[0] == city)
        gdp_index = next(i for i, x in enumerate(gdp_rank) if x[0] == city)
        rank = (0.6 * population_index) + (0.4 * gdp_index)
        weighted_rank[city] = rank

    return weighted_rank