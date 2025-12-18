"""
QUESTION:
Create a function named `find_modes` that calculates the mode(s) of a given list of numbers. The function should not use Python's statistics library. If there are multiple modes, the function should return all of them. The input list will only contain integers, and it may be empty or contain duplicate values.
"""

from collections import Counter

def find_modes(nums):
    """
    This function calculates the mode(s) of a given list of numbers.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A list of modes in the input list.
    """
    # initialize a counter for the list
    num_counter = Counter(nums)

    # get the max count
    max_count = max(num_counter.values(), default=0)

    # all numbers with max count are modes
    modes = [num for num, count in num_counter.items() if count == max_count]
    return modes