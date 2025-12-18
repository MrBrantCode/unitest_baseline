"""
QUESTION:
Write a tail-recursive Python function named `factorial` that calculates the factorial of a given number `n` without using any loops or helper functions, with a time complexity of O(1), and an initial accumulator value of 1.
"""

def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(n - 1, acc * n)