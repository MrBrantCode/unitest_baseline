"""
QUESTION:
Write a function named `sort_by_second_column` that takes a 2D list as input and returns the list sorted in ascending order by the second column value. The function should not modify the original list.
"""

def sort_by_second_column(arr):
    return sorted(arr, key=lambda x: x[1])