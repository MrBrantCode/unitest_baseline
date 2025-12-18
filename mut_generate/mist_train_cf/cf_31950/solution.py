"""
QUESTION:
Implement a function `customFloor` that takes a floating-point number `num` as input and returns the largest integer less than or equal to `num` without using any built-in floor functions or libraries. The function should handle both positive and negative floating-point numbers and return an integer as the result.
"""

def customFloor(num):
    if num >= 0:
        return int(num)
    else:
        return int(num) - 1