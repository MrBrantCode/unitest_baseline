"""
QUESTION:
Given a list of integers and a target sum, write a function `find_pairs` that finds all unique pairs of numbers in the list whose sum is equal to the target sum. The list can include both positive and negative integers. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def find_pairs(nums, required_sum):
    """
    Finds all unique pairs of numbers in the list whose sum is equal to the target sum.

    Args:
    nums (list): A list of integers.
    required_sum (int): The target sum.

    Returns:
    set: A set of unique pairs of numbers whose sum is equal to the target sum.
    """
    visited = set()
    unique_pairs = set()
    
    for num in nums:
        target = required_sum - num
        if target not in visited:
            visited.add(num)
        else:
            pair = tuple(sorted((num, target)))
            unique_pairs.add(pair)
            
    return unique_pairs