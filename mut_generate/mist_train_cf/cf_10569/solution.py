"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given number using tail recursion optimization. The function should take two parameters: `n` (the number for which the factorial is to be calculated) and an optional parameter `acc` (an accumulator that stores the intermediate result, defaulting to 1). The function should use recursion to calculate the factorial and return the result.
"""

def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(n-1, acc*n)