"""
QUESTION:
Create a function to print the first 20 Fibonacci numbers, with the loop incrementing by 3 each time, and for each Fibonacci number, print whether it is a prime number or not. Name the function to generate a prime check as 'is_prime'.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True