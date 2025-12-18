"""
QUESTION:
Write a function named `my_function` that takes an integer `x` as input. The function should continuously increment `x` by 1 as long as `x` is greater than 10 and is divisible by 3, then return the final value of `x`.
"""

def entrance(x):
    while x > 10 and x % 3 == 0:
        x += 1
    return x