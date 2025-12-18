"""
QUESTION:
Write a function `calculate_product` that calculates the product of all numbers in a given sequence that are either prime or perfect squares. The input sequence is a list of integers, and the function should return an integer representing the product of the prime and perfect square numbers in the sequence.
"""

import math

def calculate_product(sequence):
    # Function to check if number is prime
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = math.floor(math.sqrt(n))
        for i in range(3, 1 + max_div, 2):
            if n % i == 0:
                return False
        return True

    # Function to check if number is perfect square
    def is_perfect_square(n):
        if n < 0:
            return False
        root = math.sqrt(n)
        return n == int(root + 0.5) ** 2

    # Initializing product
    product = 1 

    # Iterating through the sequence
    for num in sequence:
        if is_prime(num) or is_perfect_square(num):
            product *= num

    return product