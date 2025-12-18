"""
QUESTION:
Write a function `population_decline` that simulates a population's decline over a specified number of years based on three factors: natural disasters, disease outbreak, and migration, each reducing the population by a certain percentage per year. The function should take as input the initial population size, the number of years, and the percentage reductions for each factor. It should return the final population size after the specified number of years.
"""

def population_decline(initial_population, years, natural_disaster_reduction, disease_outbreak_reduction, migration_reduction):
    """
    Simulates a population's decline over a specified number of years based on three factors.

    Args:
    initial_population (int): The initial population size.
    years (int): The number of years.
    natural_disaster_reduction (float): The percentage reduction due to natural disasters.
    disease_outbreak_reduction (float): The percentage reduction due to disease outbreak.
    migration_reduction (float): The percentage reduction due to migration.

    Returns:
    int: The final population size after the specified number of years.
    """
    population = initial_population
    for year in range(1, years + 1):
        population *= (1 - natural_disaster_reduction / 100) * (1 - disease_outbreak_reduction / 100) * (1 - migration_reduction / 100)
    return int(population)