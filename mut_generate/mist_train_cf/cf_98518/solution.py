"""
QUESTION:
Simulate a population decline over 10 years with an initial population size of 10,000. The decline is influenced by three annual factors: a 10% reduction due to natural disasters, a 5% reduction due to disease outbreak, and a 2% reduction due to migration. Write a function named `simulate_population_decline` that calculates and returns the final population size after 10 years.
"""

def simulate_population_decline(initial_population, years, disaster_factor, disease_factor, migration_factor):
    """
    Simulate a population decline over a specified number of years.

    Args:
    - initial_population (int): The initial population size.
    - years (int): The number of years to simulate.
    - disaster_factor (float): The annual reduction factor due to natural disasters.
    - disease_factor (float): The annual reduction factor due to disease outbreak.
    - migration_factor (float): The annual reduction factor due to migration.

    Returns:
    - int: The final population size after the specified number of years.
    """
    population = initial_population
    for _ in range(years):
        population *= disaster_factor
        population *= disease_factor
        population *= migration_factor
    return int(population)