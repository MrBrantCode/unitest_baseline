"""
QUESTION:
Construct a function `higher_order_func` that takes an integer `n` and a function as arguments. The function should take `n` as input and return its cube. The `higher_order_func` should calculate and return the absolute difference between the cube of `n` and `n` itself. The input function will be provided and is not required to be defined within `higher_order_func`.
"""

def higher_order_func(n, func):
    cube = func(n)
    diff = abs(cube - n)
    return diff