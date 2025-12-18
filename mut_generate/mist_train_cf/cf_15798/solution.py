"""
QUESTION:
Write a function named print_primes that prints the first n prime numbers in reverse order. The function should achieve this with a time complexity of O(n√m), where n is the index of the prime number and m is the number being checked for primality.
"""

import math

def print_primes(n):
    def is_prime(m):
        if m <= 1:
            return False
        if m <= 3:
            return True
        if m % 2 == 0 or m % 3 == 0:
            return False
        i = 5
        while i * i <= m:
            if m % i == 0 or m % (i + 2) == 0:
                return False
            i += 6
        return True

    count = 0
    i = 2
    primes = []
    while count < n:
        if is_prime(i):
            primes.append(i)
            count += 1
        i += 1
    
    for prime in reversed(primes):
        print(prime)