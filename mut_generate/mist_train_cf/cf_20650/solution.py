"""
QUESTION:
Write a function named `population_density` that takes two parameters: `population` and `land_area`. Calculate the population density by dividing the `population` by the `land_area` and return the result. The function should return the population density in people per square kilometer. Assume that the input parameters are in the correct units (people for population and square kilometers for land area).
"""

def population_density(population, land_area):
    """
    Calculate the population density by dividing the population by the land area.

    Args:
        population (int): The total population of the area.
        land_area (float): The total land area in square kilometers.

    Returns:
        float: The population density in people per square kilometer.
    """
    return population / land_area