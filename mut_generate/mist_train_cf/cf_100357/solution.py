"""
QUESTION:
Create a function `divide_by_26(num)` that takes a positive integer `num` as input, divides it by 26, and returns the result. However, if `num` is a multiple of 13, the function should return an error message instead.
"""

def divide_by_26(num):
    if num % 13 == 0:
        return "Error: Input is a multiple of 13"
    else:
        return num / 26