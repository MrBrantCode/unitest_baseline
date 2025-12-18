"""
QUESTION:
Create a function `simulate_population_decline` that calculates the final population size after a specified number of years, given the initial population size and annual reduction factors for natural disasters, disease outbreak, and migration. The function should take three parameters: `initial_population`, `years`, `disaster_factor`, `disease_factor`, and `migration_factor`, where the factors are the percentage reductions in decimal form (e.g., 10% reduction is 0.1). The function should return the final population size as an integer.
"""

def simulate_population_decline(initial_population, years, disaster_factor, disease_factor, migration_factor):
    """
    Calculate the final population size after a specified number of years, 
    given the initial population size and annual reduction factors for 
    natural disasters, disease outbreak, and migration.

    Args:
        initial_population (int): The initial population size.
        years (int): The number of years to simulate.
        disaster_factor (float): The annual reduction factor for natural disasters (in decimal form).
        disease_factor (float): The annual reduction factor for disease outbreak (in decimal form).
        migration_factor (float): The annual reduction factor for migration (in decimal form).

    Returns:
        int: The final population size as an integer.
    """
    population = initial_population
    for _ in range(years):
        population *= (1 - disaster_factor)
        population *= (1 - disease_factor)
        population *= (1 - migration_factor)
    return int(population)