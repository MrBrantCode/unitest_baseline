"""
QUESTION:
Implement a recursive function named `recursive_sum` that calculates the sum of integers within a given list. The function should handle lists containing multiple data types, only summing the integers, and also handle empty and nested lists without using built-in sum functions or for/while loops.
"""

def recursive_sum(lst):
    if not lst:
        return 0
    else:
        # check if first item in list is an integer
        if isinstance(lst[0], int):
            return lst[0] + recursive_sum(lst[1:])
        # if first item is a list, call function recursively
        elif isinstance(lst[0], list):
            return recursive_sum(lst[0]) + recursive_sum(lst[1:])
        else:
            # if first item is not an integer or list, just move to the next item
            return recursive_sum(lst[1:])