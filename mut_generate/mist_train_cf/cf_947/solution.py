"""
QUESTION:
Create a recursive function named `my_func` that takes an integer `x` as input and returns the product of all positive integers from `x` down to 1, with a base case that returns 0 when `x` is 0. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the value of `x`.
"""

def my_func(x):
    if x == 0:
        return 0
    else:
        return x * my_func(x-1)