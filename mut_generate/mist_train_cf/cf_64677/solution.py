"""
QUESTION:
Create a function named `calculate_population_density` that takes in two lists of countries, populations, capitals, and areas, and returns two dictionaries. The first dictionary should have countries as keys and their corresponding population and capital as values. The second dictionary should have countries as keys and their corresponding population density (calculated as population divided by area in square kilometers) as values, rounded to two decimal places. The areas are given in million square kilometers.
"""

def calculate_population_density(countries, populations, capitals, areas):
    """
    Creates two dictionaries. The first dictionary has countries as keys and their 
    corresponding population and capital as values. The second dictionary has 
    countries as keys and their corresponding population density (calculated as 
    population divided by area in square kilometers) as values, rounded to two 
    decimal places.

    Args:
    countries (list): A list of country names.
    populations (list): A list of population values corresponding to countries.
    capitals (list): A list of capital cities corresponding to countries.
    areas (list): A list of area values in million square kilometers corresponding to countries.

    Returns:
    tuple: A tuple of two dictionaries. The first dictionary has country details, 
    and the second dictionary has population densities.
    """

    # Create a dictionary with country details
    country_dict = {}
    for i in range(len(countries)):
        country_dict[countries[i]] = {"Population": populations[i], "Capital": capitals[i]}

    # Create another dictionary with population density
    pop_density_dict = {}
    for nation, details in country_dict.items():
        # Find the area for the current nation
        area = areas[countries.index(nation)]
        pop_density = details["Population"] / (area * 1000000)  # Since area is in million sq. km.
        pop_density_dict[nation] = round(pop_density, 2)

    return country_dict, pop_density_dict