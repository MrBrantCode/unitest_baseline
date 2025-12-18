"""
QUESTION:
Write a function `calcArea(length, width)` that calculates the area of a rectangle. The function should return the product of `length` and `width`. Assume that both `length` and `width` are non-negative. Implement a test case `test_calcArea()` to validate the function with an example where `length` is 5 and `width` is 3.
"""

def calcArea(length, width):
    assert (length >= 0)
    assert (width >= 0)
    return length * width