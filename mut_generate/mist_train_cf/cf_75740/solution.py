"""
QUESTION:
Write a function called `hypergeometric_probability` that calculates the probability of not drawing a specific group (blue balls) in a sample of a given size taken without replacement from a population with a known number of the specific group and total size. The function should take as input the total population size, the size of the specific group, and the sample size.
"""

import math

def hypergeometric_probability(total_population_size, specific_group_size, sample_size):
    """
    Calculate the probability of not drawing a specific group in a sample of a given size 
    taken without replacement from a population with a known number of the specific group and total size.

    Parameters:
    total_population_size (int): The total size of the population.
    specific_group_size (int): The size of the specific group.
    sample_size (int): The size of the sample.

    Returns:
    float: The probability of not drawing a specific group in the sample.
    """
    # Calculate the number of non-specific group members
    non_specific_group_size = total_population_size - specific_group_size

    # Calculate the total number of ways to draw the sample from the total population
    total_ways = math.comb(total_population_size, sample_size)

    # Calculate the number of ways to draw the sample from the non-specific group
    non_specific_group_ways = math.comb(non_specific_group_size, sample_size)

    # Calculate the probability of not drawing a specific group in the sample
    probability = non_specific_group_ways / total_ways

    return probability