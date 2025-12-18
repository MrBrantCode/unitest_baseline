"""
QUESTION:
Write a function named `factorial` that uses tail recursion to calculate the factorial of a given number. The function should take two parameters: `n` (the number to calculate the factorial of) and an optional `accumulator` parameter to store the intermediate result. The function should return the final factorial result. Implement the function in a way that allows for potential tail call optimization by compilers and interpreters.
"""

def factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return factorial(n-1, accumulator * n)