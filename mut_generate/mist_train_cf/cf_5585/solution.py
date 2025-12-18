"""
QUESTION:
Design a function `is_prime` that determines whether a given number is prime or not. The function should take a single integer argument `n` greater than 1, have a time complexity of O(sqrt(n)), and not use any external libraries. The function should return `True` if `n` is prime and `False` otherwise. 

Additionally, write a try/except block that takes user input, checks if the input is a valid integer greater than 1, calls the `is_prime` function, and prints whether the number is prime or not. The block should handle non-integer inputs and display an appropriate error message.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True