"""
QUESTION:
Implement a function named `factorial` that calculates the factorial of a given non-negative integer `n` using tail recursion. The function should take an optional second parameter `acc` with a default value of 1, which is used to accumulate the intermediate results. The function should return the factorial of `n`.
"""

def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(n - 1, acc * n)