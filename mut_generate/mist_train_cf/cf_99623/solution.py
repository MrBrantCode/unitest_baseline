"""
QUESTION:
Write a function named `simulate_population_decline` that calculates the final population size after a specified number of years, given the initial population size and the annual reduction rates due to natural disasters, disease outbreak, and migration. The function should take four parameters: `initial_population`, `disaster_rate`, `disease_rate`, and `migration_rate`, and `years`, and return the final population size after the specified number of years. Assume the reduction rates are percentages expressed as decimal values (e.g., 10% is 0.10).
"""

def simulate_population_decline(initial_population, disaster_rate, disease_rate, migration_rate, years):
    """
    Calculate the final population size after a specified number of years.

    Parameters:
    initial_population (int): The initial population size.
    disaster_rate (float): The annual reduction rate due to natural disasters.
    disease_rate (float): The annual reduction rate due to disease outbreak.
    migration_rate (float): The annual reduction rate due to migration.
    years (int): The number of years.

    Returns:
    int: The final population size after the specified number of years.
    """
    population = initial_population
    for _ in range(years):
        population *= (1 - disaster_rate) * (1 - disease_rate) * (1 - migration_rate)
    return int(population)