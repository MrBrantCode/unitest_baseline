"""
QUESTION:
Find the smallest odd number from a given list of positive integers (ranging from 1 to 1,000,000,000) without using built-in or helper functions, recursion, or any extra space besides a constant number of variables. The list can have up to 1,000,000 elements and may contain duplicate elements, but will never contain zeros or negative numbers. The time complexity of your solution should not exceed O(n).

Complete this code:

def smallest_odd_number(l: list)
"""

def entance(l: list):
    """Return the smallest odd number in the list."""
    smallest = float('inf')
    for num in l:
        if num % 2 != 0 and num < smallest:
            smallest = num
    return smallest