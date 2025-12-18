"""
QUESTION:
Given a set of three distinct categories of cereal grains - wheat, rice, and corn with initial weights of 2 kilograms, 3 kilograms, and 1 kilogram respectively, create a function `calculate_grain_weights` to calculate the weights of each grain type required to achieve a composite package of a specified target weight while maintaining the relative proportions of the grain types. The function should take the target weight as input and return the weights of wheat, rice, and corn.
"""

def calculate_grain_weights(target_weight):
    """
    Calculate the weights of each grain type required to achieve a composite package of a specified target weight
    while maintaining the relative proportions of the grain types.

    Args:
        target_weight (float): The target weight of the composite package.

    Returns:
        tuple: A tuple containing the weights of wheat, rice, and corn respectively.
    """
    # Define the initial weights of wheat, rice, and corn
    wheat_weight = 2
    rice_weight = 3
    corn_weight = 1

    # Calculate the total initial weight
    total_initial_weight = wheat_weight + rice_weight + corn_weight

    # Calculate the multiplier to achieve the target weight while maintaining the relative proportions
    multiplier = target_weight / total_initial_weight

    # Calculate the weights of wheat, rice, and corn required to achieve the target weight
    wheat_required = wheat_weight * multiplier
    rice_required = rice_weight * multiplier
    corn_required = corn_weight * multiplier

    return wheat_required, rice_required, corn_required