"""
QUESTION:
Write a function named `calculate_sugar_requirements` that determines the sugar requirements for making two different types of candy. The function takes the total weight of candy and the sugar-to-candy ratio for each type as input. The sugar-to-candy ratios are represented as a list or tuple of two floats where the first element is the sugar-to-candy ratio for the first type of candy and the second element is the sugar-to-candy ratio for the second type of candy. The function should return the amount of sugar required for each type of candy to make the total weight of candy, assuming the total weight is divided equally between the two types.
"""

def calculate_sugar_requirements(total_weight, sugar_to_candy_ratios):
    """
    Calculates the sugar requirements for making two different types of candy.

    Args:
    total_weight (float): The total weight of candy.
    sugar_to_candy_ratios (list or tuple): A list or tuple of two floats representing the sugar-to-candy ratios for each type of candy.

    Returns:
    tuple: A tuple of two floats representing the amount of sugar required for each type of candy.
    """
    # Calculate the weight of each type of candy
    weight_per_type = total_weight / 2
    
    # Calculate the sugar required for each type of candy
    sugar_required = [weight_per_type * ratio for ratio in sugar_to_candy_ratios]
    
    return tuple(sugar_required)