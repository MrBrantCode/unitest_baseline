"""
QUESTION:
Determine the minimum amount of each type of grape (3kg, 2kg, 1kg) needed to reach a total weight of 20kg, using at least 2 of each type of grape.
"""

def min_grapes(total_weight):
    """
    Calculate the minimum amount of each type of grape (3kg, 2kg, 1kg) needed to reach a total weight.
    
    Parameters:
    total_weight (int): The total weight needed.
    
    Returns:
    tuple: A tuple containing the minimum amount of each type of grape.
    """
    # Calculate the weight of 2 of each type of grape
    base_weight = 2 * 3 + 2 * 2 + 2 * 1
    
    # Calculate the remaining weight
    remaining_weight = total_weight - base_weight
    
    # Calculate the number of 3kg grapes needed
    three_kg_grapes = 2 + remaining_weight // 3 + (1 if remaining_weight % 3 != 0 else 0)
    
    # The number of 2kg and 1kg grapes is 2 each
    two_kg_grapes = 2
    one_kg_grapes = 2
    
    return three_kg_grapes, two_kg_grapes, one_kg_grapes