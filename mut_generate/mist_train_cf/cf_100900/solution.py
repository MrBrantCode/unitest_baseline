"""
QUESTION:
Create a function named `calculate_weighted_rank` to calculate the weighted rank of cities based on their population sizes and GDP per capita. The function should take a dictionary of city data as input, where each city is a key and its corresponding value is another dictionary containing the city's population size and GDP per capita. The GDP per capita should have a weight of 0.4. The function should return a dictionary with the city names as keys and their corresponding weighted ranks as values.
"""

def calculate_weighted_rank(city_data):
    """
    Calculate the weighted rank of cities based on their population sizes and GDP per capita.
    
    Args:
        city_data (dict): A dictionary of city data, where each city is a key and its corresponding value is another dictionary containing the city's population size and GDP per capita.
    
    Returns:
        dict: A dictionary with the city names as keys and their corresponding weighted ranks as values.
    """
    # Calculate population rank
    population_rank = sorted(city_data.items(), key=lambda x: x[1]['population'], reverse=True)
    # Calculate GDP per capita rank
    gdp_rank = sorted(city_data.items(), key=lambda x: x[1]['gdp_per_capita'], reverse=True)
    # Calculate weighted rank
    weighted_rank = {}
    for city in city_data:
        population_index = next(i for i, x in enumerate(population_rank) if x[0] == city)
        gdp_index = next(i for i, x in enumerate(gdp_rank) if x[0] == city)
        rank = (0.6 * population_index) + (0.4 * gdp_index)
        weighted_rank[city] = rank
    return weighted_rank