"""
QUESTION:
Write a function `factorial(n, acc=1)` that calculates the factorial of a given number `n` using tail recursion optimization. The function should return an error message if `n` is negative. Assume `n` is an integer and `n` is greater than or equal to -infinity and `acc` is greater than or equal to 0.
"""

def entance(n, acc=1):
    if n < 0:
        return "Error: Factorial of a negative number is undefined."
    elif n == 0:
        return acc
    else:
        return entance(n - 1, acc * n)