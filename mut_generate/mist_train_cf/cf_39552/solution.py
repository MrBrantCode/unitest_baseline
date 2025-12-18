"""
QUESTION:
Write a Python function named `process_population_data` that takes two inputs: a 2D array `populations` where each row represents a year and each column represents a species, and a 1D array `years`. The function should calculate the standard deviation of the populations for each species, determine the year with the maximum population for each species, identify the species with the maximum population for each year, and determine if any species had a population exceeding 50,000 in any year. The function should use NumPy and return the required output as specified above.
"""

import numpy as np

def process_population_data(populations, years):
    # Calculate the standard deviation of the populations for each species
    std_dev = populations.std(axis=0)

    # Determine the year with the maximum population for each species
    max_years = years[np.argmax(populations, axis=0)]

    # Identify the species with the maximum population for each year
    max_species = np.argmax(populations, axis=1)

    # Determine if any species had a population exceeding 50,000 in any year
    above_50000 = np.any(populations > 50000, axis=0)

    return std_dev, max_years, max_species, above_50000