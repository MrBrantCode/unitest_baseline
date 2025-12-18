"""
QUESTION:
Implement a function called `custom_sort` that takes a 2D list of integers as input and returns the sorted list. The list should be sorted by the second element of the sublists in descending order. If the second elements are equal, the sublists should be sorted by their third element in ascending order.
"""

def custom_sort(lst):
    return sorted(lst, key=lambda x: (-x[1], x[2]))