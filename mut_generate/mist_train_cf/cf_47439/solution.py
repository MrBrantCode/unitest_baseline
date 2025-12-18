"""
QUESTION:
Create a function `is_symmetric(num)` that takes an integer `num` as input and returns `True` if the numerical sequence is the same when read from left to right and right to left, and `False` otherwise.
"""

def is_symmetric(num):
    return str(num) == str(num)[::-1]