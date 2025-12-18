"""
QUESTION:
Write a function named `sum_of_cubes_in_range` that takes a list of integers and a range defined by `min_val` and `max_val`, and returns `True` if the sum of the cubes of all integers in the list falls within the inclusive range, and `False` otherwise. The function should handle any list of integers and any range.
"""

def sum_of_cubes_in_range(lst: list, min_val: int, max_val: int) -> bool:
    """Find out if the sum of cubes of all elements in the list is within the range."""
    sum_of_cubes = sum(i**3 for i in lst)
    return min_val <= sum_of_cubes <= max_val