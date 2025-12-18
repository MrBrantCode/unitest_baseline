"""
QUESTION:
Write a function `find_prime_numbers(n)` that finds all prime numbers up to `n` and returns them in descending order, with a time complexity of O(n*log(log(n))) and a space complexity of O(n).
"""

import math

def find_prime_numbers(n):
    # Create a boolean array "is_prime[0..n]" and initialize all entries it as true
    is_prime = [True] * (n + 1)
    prime_numbers = []

    # Mark numbers smaller than 2 as not prime
    is_prime[0] = is_prime[1] = False

    # Loop through all numbers up to square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            # If is_prime[i] is true, it is a prime number, so add it to the list
            prime_numbers.append(i)

            # Mark all multiples of i as not prime
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Add remaining prime numbers to the list
    for i in range(int(math.sqrt(n)) + 1, n + 1):
        if is_prime[i]:
            prime_numbers.append(i)

    # Return prime numbers in descending order
    return prime_numbers[::-1]