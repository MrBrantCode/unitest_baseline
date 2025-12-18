"""
QUESTION:
Create a function called `first_non_repeating_prime` that takes an array of integers as input and returns the first non-repeating prime number in the array. The function should consider both positive and negative integers, but only return a non-repeating prime number if it exists. If no non-repeating prime numbers are found, return None.
"""

def firstNonRepeatingPrime(array):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in array if is_prime(abs(num))]
    for prime in primes:
        if primes.count(prime) == 1:
            return prime
    return None