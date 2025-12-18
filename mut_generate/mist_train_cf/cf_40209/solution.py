"""
QUESTION:
Write a function `find_min_non_negative` that takes a list of integers as input and assigns the minimum non-negative integer to the variable `finalmn`. If there are no non-negative integers in the list, `finalmn` should be assigned the value -1.
"""

from typing import List

def find_min_non_negative(vals: List[int]) -> int:
    """
    This function finds the minimum non-negative integer in a given list.
    
    Args:
    vals (List[int]): A list of integers.
    
    Returns:
    int: The minimum non-negative integer if found, -1 otherwise.
    """
    finalmn = -1  # Initialize finalmn to -1
    for val in vals:
        if val >= 0 and (finalmn == -1 or val < finalmn):
            finalmn = val  # Update finalmn if val is non-negative and smaller than the current finalmn
    return finalmn