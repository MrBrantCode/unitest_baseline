"""
QUESTION:
Create a function named 'is_prime' that determines whether a given positive integer is a prime number or not, using an efficient time complexity of O(sqrt(n)), without relying on built-in libraries or functions that directly check if a number is prime, and without using trial division or brute force methods.
"""

import math

def is_prime(n):
    # Check if n is 0 or 1
    if n <= 1:
        return False

    # Create a boolean array to track prime numbers
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    # Iterate through numbers from 2 to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            # Set all multiples of i as non-prime
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return is_prime[n]