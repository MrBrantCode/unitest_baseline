"""
QUESTION:
Write a recursive function named `factorial` that takes an integer `num` as input and returns the factorial of `num`, with the restriction that `num` must be a non-negative integer. The function should use recursive calls to calculate the factorial.
"""

def factorial(num):
    # base case
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)