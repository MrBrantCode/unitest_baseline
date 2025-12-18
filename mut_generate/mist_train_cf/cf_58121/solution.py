"""
QUESTION:
Write a function `check_none` that takes a tuple as input. The function should return a boolean indicating whether the tuple contains any `None` values and the index of the first `None` value if found. If no `None` values are found, return the index as `-1`.
"""

def check_none(input_tuple):
    if None in input_tuple:
        return True, input_tuple.index(None)
    else:
        return False, -1