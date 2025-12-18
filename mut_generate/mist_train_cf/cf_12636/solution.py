"""
QUESTION:
Write a function named `find_pairs` that takes a list of integers and a target sum as input, and returns a list of tuples, where each tuple contains the indices of two elements in the list whose sum is equal to the target sum. The function should return all such pairs and the indices in the output tuples should be in ascending order.
"""

def find_pairs(lst, target):
    """
    This function finds all pairs of elements in the given list whose sum equals the target sum.
    
    Args:
        lst (list): A list of integers.
        target (int): The target sum.
    
    Returns:
        list: A list of tuples, where each tuple contains the indices of two elements in the list whose sum is equal to the target sum.
    """
    pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((i, j))
    return pairs