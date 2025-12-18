"""
QUESTION:
Implement a recursive function `add_one_recursive` that takes a list of integers as input, adds 1 to each element, and returns a new list with the results. The original list should remain unchanged. The function should handle lists of any length, including empty lists.
"""

def add_one_recursive(lst):
    if len(lst) == 0:
        return []
    else:
        return [lst[0] + 1] + add_one_recursive(lst[1:])