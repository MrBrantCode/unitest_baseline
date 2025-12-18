"""
QUESTION:
Write a function `shannon_diversity_index(species_abundance)` that calculates the Shannon Diversity Index for a given set of species abundance data. The function should take a dictionary `species_abundance` as input where the keys are the species names and the values are the abundance or count of each species. The function should return the calculated Shannon Diversity Index, which is defined as -Σ(pi * ln(pi)), where pi is the proportion of individuals of the ith species relative to the total number of individuals in the community.
"""

import math

def shannon_diversity_index(species_abundance):
    total_count = sum(species_abundance.values())
    proportions = [count / total_count for count in species_abundance.values()]
    shannon_index = -sum(p * math.log(p) for p in proportions if p != 0)
    return shannon_index