"""
QUESTION:
Create a function `make_negative` that takes an integer `num` as input and returns its negative value if it is positive, and returns the input value as is if it is already negative or zero.
"""

def make_negative(num):
    return -num if num > 0 else num