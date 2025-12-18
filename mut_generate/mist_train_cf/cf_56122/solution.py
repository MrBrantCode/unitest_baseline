"""
QUESTION:
Implement a function named `reverse` that takes a list of integers (positive and negative) as input and returns the reversed list using recursion. The function should handle lists of any size, including empty lists.
"""

def reverse(lst):
    # Base Case: An empty list should return a new empty list
    if len(lst) == 0:
        return []

    # Recursive case: add the last element of the list to a new list and reverse the rest of the list
    return [lst[-1]] + reverse(lst[:-1])