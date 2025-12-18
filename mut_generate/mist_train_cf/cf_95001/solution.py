"""
QUESTION:
Write a function named recursive_sum that calculates the sum of all integers in a list and its nested lists, ignoring any non-integer elements. The function should have a time complexity of O(n), where n is the total number of elements, and should not use any built-in sum() function or loop structure.

The function should take a single argument, which can be a list containing integers and/or nested lists, or a single integer. If the argument is a list, the function should recursively calculate the sum of all integers within the list and its nested lists. If the argument is a single integer, the function should return the integer.
"""

def entance(lst):
    if isinstance(lst, int):
        return lst
    elif isinstance(lst, list):
        return sum(entance(x) for x in lst if isinstance(x, (int, list)))
    else:
        return 0