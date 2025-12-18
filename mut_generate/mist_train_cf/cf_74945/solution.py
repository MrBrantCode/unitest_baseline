"""
QUESTION:
Find the possible quantities of 20-gram candies and 30-gram candies that add up to a combined weight of 600 grams.
"""

def entrance(total_weight, weight1, weight2):
    """
    Find the possible quantities of candies with weights weight1 and weight2 
    that add up to a combined weight of total_weight.

    Args:
        total_weight (int): The total weight of all candies.
        weight1 (int): The weight of the first type of candy.
        weight2 (int): The weight of the second type of candy.

    Returns:
        A list of tuples, where each tuple contains the possible quantities of 
        candies with weights weight1 and weight2.
    """
    combinations = []
    for x in range(total_weight // weight1 + 1):
        y = (total_weight - x * weight1) / weight2
        if y == int(y):
            combinations.append((x, int(y)))
    return combinations