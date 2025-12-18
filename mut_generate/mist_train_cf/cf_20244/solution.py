"""
QUESTION:
Implement a function called `factorial` that takes an integer `n` and calculates its factorial using tail recursion. The function should use an accumulator variable to store intermediate results, since Python does not optimize tail recursion. The function should be able to handle non-negative integer inputs, including 0, and return the correct factorial result.
"""

def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(n - 1, acc * n)