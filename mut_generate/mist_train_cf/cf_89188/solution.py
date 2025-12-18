"""
QUESTION:
Create a function named `double_and_filter` that takes a list of integers as input. The function should return a new list where each element from the input list is doubled, duplicates are removed, and only elements divisible by 3 are included. The resulting list should be sorted in descending order. The original input list should remain unchanged.
"""

def double_and_filter(lst):
    return sorted([2 * x for x in set(lst) if (2 * x) % 3 == 0], reverse=True)