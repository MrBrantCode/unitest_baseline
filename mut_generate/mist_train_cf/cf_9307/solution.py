"""
QUESTION:
Write a Python function `factorial(n, acc=1)` to calculate the factorial of a non-negative integer `n` using tail recursion. The function should take two parameters: `n` (the input number) and an optional parameter `acc` (the accumulator, default value is 1). The function should return the factorial of `n` as the result.
"""

def entrance(n, acc=1):
    if n == 0:
        return acc
    else:
        return entrance(n - 1, acc * n)