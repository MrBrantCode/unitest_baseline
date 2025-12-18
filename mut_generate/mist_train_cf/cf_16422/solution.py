"""
QUESTION:
Write a function `factorial(n, acc=1)` that calculates the factorial of a number `n` using tail recursion, where `acc` is an accumulator for the result. The function should reuse the same stack frame for each recursive call to avoid stack overflow errors.
"""

def entance(n, acc=1):
    if n == 0:
        return acc
    else:
        return entance(n - 1, acc * n)