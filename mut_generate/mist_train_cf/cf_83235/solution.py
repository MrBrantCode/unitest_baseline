"""
QUESTION:
Design a data structure to store prime numbers up to a given number 'n', where 'n' is 1 million in this case, that optimizes both storage and retrieval operations. Implement a function named `generate_primes` that takes an integer 'n' as input and returns a boolean array where each index represents a number and its corresponding value indicates whether the number is prime or not. The solution should have efficient storage and retrieval operations, with retrieval being a constant time operation.
"""

import math

def generate_primes(n):
    """
    Generates a boolean array where each index represents a number and its corresponding value indicates whether the number is prime or not.

    Args:
        n (int): The upper limit up to which primes are generated.

    Returns:
        list: A boolean array where each index represents a number and its corresponding value indicates whether the number is prime or not.
    """
    # initially all numbers are prime (i.e., value = True)
    prime = [True for i in range(n+1)]

    # we know 0 and 1 are not primes
    prime[0] = prime[1] = False

    p = 2
    while(p * p <= n):
        # If prime[p] is still prime, then mark all multiples as not prime
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # now the array contains True at the prime indexes and False otherwise
    return prime