"""
QUESTION:
Write a function `get_primes(num)` that returns a list of prime numbers in the range from 2 to `num` (inclusive). The function should take an integer `num` as input and return a list of integers. The list should contain all numbers in the given range that can only be divided by 1 or themselves.
"""

def get_primes(num):
    '''Return list representing the prime numbers in the range from 2 to num (inclusive)'''
    
    # Create a list containing only True values.
    sieve = [True] * (num + 1)
    primes = []

    # Start from the first prime number, which is 2.
    for current_prime in range(2, num + 1):

        # If the current number has not been crossed off, it is a prime
        if (sieve[current_prime]):

            # Include the prime number in our list
            primes.append(current_prime)

            # Cross off all multiples of current_prime (they are not prime)
            for multiple in range(current_prime * 2, num + 1, current_prime):
                sieve[multiple] = False

    return primes