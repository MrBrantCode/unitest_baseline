"""
QUESTION:
Write a function `recursive_sum` that calculates the sum of all integers in a given list using recursion. The function should take a list of integers as input and return the sum as an integer.
"""

def recursive_sum(lst): 
    # Base case
    if not len(lst): 
        return 0
    return lst[0] + recursive_sum(lst[1:])