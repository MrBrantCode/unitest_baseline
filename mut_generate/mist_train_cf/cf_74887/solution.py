"""
QUESTION:
Create a function called `calculate_grain_proportions` that takes in the total weight of a mixed grain package and the weights of three distinct grain varieties. The function should return the weight contribution of each grain type to compile the mixed grain package with proper equal proportion distribution.
"""

def calculate_grain_proportions(total_weight, wheat_weight, rice_weight, corn_weight):
    """
    Calculate the weight contribution of each grain type to compile the mixed grain package with proper equal proportion distribution.

    Args:
        total_weight (float): The total weight of the mixed grain package.
        wheat_weight (float): The weight of wheat grain.
        rice_weight (float): The weight of rice grain.
        corn_weight (float): The weight of corn grain.

    Returns:
        tuple: A tuple containing the weight contribution of wheat, rice, and corn grains.
    """
    total_grain_weight = wheat_weight + rice_weight + corn_weight
    sets = total_weight / total_grain_weight
    wheat_contribution = wheat_weight * sets
    rice_contribution = rice_weight * sets
    corn_contribution = corn_weight * sets
    return wheat_contribution, rice_contribution, corn_contribution