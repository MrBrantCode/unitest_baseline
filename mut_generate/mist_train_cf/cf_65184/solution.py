"""
QUESTION:
Write a function `calculate_factorial(num)` that takes an integer `num` as input and returns its factorial using recursion. The function should have a base condition to stop the recursion.
"""

def calculate_factorial(num):
    # Base condition
    if num == 0:
        return 1
    else:
        return num * calculate_factorial(num-1)