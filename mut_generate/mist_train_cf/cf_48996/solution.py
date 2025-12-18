"""
QUESTION:
Write a recursive function `recursive_sum` that takes two arguments `a` and `b` with default values of 0, and calculates the sum of two numbers until it reaches the value 42. The function should not require any input arguments when called.
"""

def recursive_sum(a=0, b=0):
    if a == 42:
        return a
    elif a < 42:
        return recursive_sum(a+1, b)