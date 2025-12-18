"""
QUESTION:
Write a function named `my_function` that takes an integer `x` as input. The function should continuously increment `x` by 1 as long as `x` is greater than 1000 and is divisible by 3, and return the final value of `x` after the loop terminates.
"""

def entrance(x):
    while x > 1000 and x % 3 == 0:
        x += 1
    return x