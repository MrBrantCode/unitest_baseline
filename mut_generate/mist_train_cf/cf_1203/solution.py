"""
QUESTION:
Implement a function `is_prime(num)` that checks if a number is prime, and use it in a while loop to print all prime numbers from 2 to 1000. The time complexity of the solution should be O(n√n), where n is the input number 1000.
"""

import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True