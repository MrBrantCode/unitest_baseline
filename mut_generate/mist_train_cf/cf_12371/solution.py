"""
QUESTION:
Write a function `f(x)` to calculate the `x`th number in the Fibonacci sequence, where each number is the sum of the two preceding ones, starting from 0 and 1. The function should use recursion and have base cases `f(0) = 1` and `f(1) = 1`.
"""

def f(x):
    # base cases
    if x == 0:
        return 0
    elif x == 1:
        return 1
    # recursive case
    else:
        return f(x-1) + f(x-2)