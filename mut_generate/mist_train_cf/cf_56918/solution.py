"""
QUESTION:
Write a function called `max_consecutive_sum` that takes a list of integers as input and returns the maximum cumulative sum of four consecutive integers within the list. The function should return the maximum cumulative sum, not the subsequence itself. The function should be able to handle lists with less than four elements, in which case it should return the maximum cumulative sum of the entire list.
"""

from itertools import islice

def max_consecutive_sum(nums):
    """
    Returns the maximum cumulative sum of four consecutive integers within the list.
    
    If the list has less than four elements, it returns the maximum cumulative sum of the entire list.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        int: The maximum cumulative sum of four consecutive integers.
    """
    n = min(4, len(nums))  # adjust the window size if the list has less than 4 elements
    it = iter(nums)
    result = tuple(islice(it, n))
    max_sum = sum(result)
    for elem in it:
        result = result[1:] + (elem,)
        max_sum = max(max_sum, sum(result))
    return max_sum