"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given number using tail recursion. The function should take two parameters: `n` (the number for which the factorial is calculated) and `acc` (an accumulator variable with a default value of 1). Implement the base case and use the accumulator variable to optimize the function.
"""

def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(n - 1, acc * n)