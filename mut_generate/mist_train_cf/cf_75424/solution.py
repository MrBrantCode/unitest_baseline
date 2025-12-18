"""
QUESTION:
Write a function `check_existence(x, list)` that takes an integer `x` and a list of integers as input and returns a string indicating whether `x` exists in the list. The function should return "x exists in the list" if `x` is in the list, and "x does not exist in the list" otherwise.
"""

def check_existence(x, lst):
    if x in lst:
        return str(x) + " exists in the list"
    else:
        return str(x) + " does not exist in the list"