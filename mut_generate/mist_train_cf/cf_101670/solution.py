"""
QUESTION:
Write a Python function `simulate_population_decline` that calculates the final population size after applying natural disaster, disease outbreak, and migration factors for a specified number of years. The function should take the initial population size, natural disaster reduction rate, disease outbreak reduction rate, migration reduction rate, and the number of years as input parameters. The function should return the final population size. 

Restrictions: The reduction rates should be percentages in decimal form (e.g., 10% = 0.1).
"""

def simulate_population_decline(initial_population, natural_disaster_rate, disease_outbreak_rate, migration_rate, years):
    """
    Calculate the final population size after applying natural disaster, disease outbreak, and migration factors.

    Args:
        initial_population (float): The initial population size.
        natural_disaster_rate (float): The natural disaster reduction rate in decimal form (e.g., 10% = 0.1).
        disease_outbreak_rate (float): The disease outbreak reduction rate in decimal form (e.g., 10% = 0.1).
        migration_rate (float): The migration reduction rate in decimal form (e.g., 10% = 0.1).
        years (int): The number of years.

    Returns:
        float: The final population size.
    """

    # Apply the reduction factors for each year
    for _ in range(years):
        initial_population *= (1 - natural_disaster_rate)  # Apply natural disaster factor
        initial_population *= (1 - disease_outbreak_rate)  # Apply disease outbreak factor
        initial_population *= (1 - migration_rate)  # Apply migration factor

    return initial_population