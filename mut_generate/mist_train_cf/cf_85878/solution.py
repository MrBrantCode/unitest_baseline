"""
QUESTION:
Create a function called `subset_check` that checks if one set is a subset of another without using Python's built-in set methods like `issubset()`. The function should take two sets as input and return `True` if the first set is a subset of the second set and `False` otherwise. Note that the function is not allowed to use any Python built-in set methods, but built-in Python functions like `all()` are allowed.
"""

def subset_check(s1: set, s2: set):
    return all(item in s2 for item in s1)