"""
QUESTION:
Implement a function called `recursive_sum` that calculates the sum of all integers in a nested list. The list may contain integers, strings, and other lists. Ignore non-integer elements. Use recursion to handle nested lists.
"""

def recursive_sum(lst):
    total = 0
    for element in lst:
        if isinstance(element, int):
            total += element
        elif isinstance(element, list):
            total += recursive_sum(element)
    return total