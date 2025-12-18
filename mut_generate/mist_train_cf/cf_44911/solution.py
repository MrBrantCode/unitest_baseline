"""
QUESTION:
Write a function `is_count_in_range` that takes a string and two optional integer parameters `a` and `b` (defaulting to 5 and 15, respectively) and returns `True` if the length of the string is within the range [a, b] and `False` otherwise.
"""

def is_count_in_range(text, a=5, b=15):
    return a <= len(text) <= b