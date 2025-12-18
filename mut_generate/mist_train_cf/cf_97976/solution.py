"""
QUESTION:
Write a function named `percentage_of_expatriates` that calculates the percentage of expatriates in the UAE compared to the entire population without using loops. The function should take two parameters: `total_population` and `expat_population`, and return the calculated percentage.
"""

def percentage_of_expatriates(total_population, expat_population):
    """
    Calculates the percentage of expatriates in the UAE.

    Args:
    total_population (int): Total population of the UAE.
    expat_population (int): Population of expatriates in the UAE.

    Returns:
    float: Percentage of expatriates in the UAE.
    """
    if total_population == 0:
        return 0
    else:
        return (expat_population / total_population) * 100