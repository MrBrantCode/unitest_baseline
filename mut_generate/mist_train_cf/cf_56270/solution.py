"""
QUESTION:
Write a function `is_perfect_square(n)` to check if a number is a perfect square and then use it to replace perfect squares in a Fibonacci series with four times their value. The function should take an integer `n` as input and return a boolean indicating whether `n` is a perfect square.
"""

def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n