"""
QUESTION:
Create a function named `calculate_odd_product` that takes one integer argument `n` where `n` is a positive integer greater than or equal to 1. The function should return the product of all odd numbers between 1 and `n` (inclusive). The function should be implemented with an efficiency that avoids unnecessary checks for even numbers.
"""

def calculate_odd_product(n):
    product = 1
    for i in range(1, n+1, 2):
        product *= i
    return product