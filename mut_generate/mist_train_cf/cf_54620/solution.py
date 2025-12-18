"""
QUESTION:
Write a Python function `get_sum(a, b)` that takes two arguments `a` and `b`. The function should return their sum if both arguments are numbers (either integer or float) and concatenate them if they are strings. If the data types of `a` and `b` are not the same, or if they are neither numbers nor strings, the function should return an error message.
"""

def get_sum(a, b):
    if type(a) != type(b):
        return "Error: The types of the input parameters are not the same."
    else:
        if isinstance(a, (int, float)):
            return a+b
        elif isinstance(a, str):
            return a+b
        else:
            return "Error: The function only supports numbers and strings."