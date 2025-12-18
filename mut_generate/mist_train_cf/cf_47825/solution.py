"""
QUESTION:
Create a function named `largest_common_divisor` that takes two lists of integers, `list1` and `list2`, as input. The function should calculate the largest common divisor for each pair of integers (A,B) where A is from `list1` and B is from `list2` with the same index. Return a new list containing the largest common divisor for each pair. The function must implement the Euclidean algorithm and include validation checks to ensure both input lists are non-empty and of the same length.
"""

from math import gcd

def largest_common_divisor(list1, list2):
    # check if both lists have the same length
    if len(list1) != len(list2):
        return "Error: lists must have the same length"
    
    # check each list is non-empty
    if not list1 or not list2:
        return "Error: lists must be non-empty"
    
    # calculate gcd for each pair (A, B)
    return [gcd(A, B) for A, B in zip(list1, list2)]