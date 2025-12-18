"""
QUESTION:
Write a function named `calculate_baskets` that takes the total number of apples and the number of apples per basket as input, and returns the maximum number of whole gift baskets that can be created. The function should use integer division to ensure a whole number of baskets is returned.
"""

def calculate_baskets(total_apples, apples_per_basket):
    """
    Calculate the maximum number of whole gift baskets that can be created.

    Args:
        total_apples (int): The total number of apples.
        apples_per_basket (int): The number of apples per basket.

    Returns:
        int: The maximum number of whole gift baskets that can be created.
    """
    return total_apples // apples_per_basket