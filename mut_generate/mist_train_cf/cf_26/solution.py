"""
QUESTION:
Create a function named `is_prime` that takes an integer as input and returns "Prime" if the number is prime, otherwise returns "Composite". The function should have a time complexity of O(n) or better and should not use any built-in functions or libraries to check for primality, with the exception of math.sqrt for optimization.
"""

import math

def is_prime(num):
    if num <= 1:
        return "Composite"

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return "Composite"

    return "Prime"