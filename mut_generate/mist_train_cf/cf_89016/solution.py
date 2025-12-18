"""
QUESTION:
Create a function named `is_prime` that takes a positive integer `n` as input and returns a boolean value indicating whether `n` is a prime number or not. A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. You cannot use built-in libraries or functions that directly check if a number is prime. Implement an efficient algorithm with a time complexity better than trial division or brute force methods.
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