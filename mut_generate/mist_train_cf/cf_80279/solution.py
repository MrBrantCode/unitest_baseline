"""
QUESTION:
Create a function named `within_range` that takes a list of integers and a range defined by `lower_limit` and `upper_limit`, and returns `True` if every number in the list is within the range, and `False` otherwise.
"""

def within_range(lst: list, lower_limit: int, upper_limit: int) -> bool:
    return all(lower_limit <= item <= upper_limit for item in lst)