"""
QUESTION:
Create a function `product(n)` that calculates the product of numbers from 1 to `n` (inclusive), considering only odd numbers if `n` is odd and only even numbers if `n` is even. The function should assume that `n` is a positive integer.
"""

def product(n):
    # Initialize the product and the starting number
    if n % 2 == 0:
        product = 1
        start = 2
    else:
        product = 1
        start = 1

    # Compute the product of the numbers
    while start <= n:
        product *= start
        start += 2

    return product