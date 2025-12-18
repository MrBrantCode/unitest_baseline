"""
QUESTION:
Write a function named `isPerfectSquare` to determine if a given number is a perfect square without using any built-in square root or power functions. The function should return `True` if the number is a perfect square and `False` otherwise. The input `n` will be a positive integer.
"""

def isPerfectSquare(n):
    i = 1
    while n > 0:
        n -= i
        i += 2
    return n == 0