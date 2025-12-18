"""
QUESTION:
Write a tail-recursive function named `factorial` that calculates the factorial of a number `n` with a time complexity of O(1) without using any loops or helper functions. The function should have an additional parameter to keep track of the running product, which defaults to 1.
"""

def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(n - 1, acc * n)