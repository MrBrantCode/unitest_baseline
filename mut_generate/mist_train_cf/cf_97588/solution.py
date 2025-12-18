"""
QUESTION:
Create a function `find_valid_pairs` that takes a list of unique integers `numbers` and an integer `target_sum` as input. The function should return all possible pairs of numbers from the list that have a sum equal to `target_sum`, without repeating any pairs or using the same number twice.
"""

def find_valid_pairs(numbers, target_sum):
    """
    Find all possible pairs of numbers from the list that have a sum equal to target_sum.
    
    Args:
    numbers (list): A list of unique integers.
    target_sum (int): The target sum.
    
    Returns:
    list: A list of pairs of numbers with a sum equal to target_sum.
    """
    import itertools
    # Use itertools to generate all possible combinations of length 2
    combinations = itertools.combinations(numbers, 2)
    # Filter the combinations to only include those that have the same sum
    valid_pairs = [pair for pair in combinations if sum(pair) == target_sum]
    return valid_pairs