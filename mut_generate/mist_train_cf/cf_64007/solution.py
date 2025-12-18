"""
QUESTION:
Create a function `get_prime_multiplication_table(n)` that generates a 2D array containing a multiplication table for prime numbers between 0 and `n`, excluding prime numbers whose digital root equals 3. The digital root of a number is the recursive sum of its digits until a single-digit number is obtained. The function should return the 2D multiplication table.
"""

import numpy as np

def calculate_digital_root(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for x in range(2, int(n ** .5) + 1):
        if n % x == 0:
            return False
    return True

def get_prime_multiplication_table(n):
    primes = [possiblePrime for possiblePrime in range(2, n + 1) 
              if is_prime(possiblePrime) and calculate_digital_root(possiblePrime) != 3]
    table = np.empty((len(primes), len(primes)))
    for i in range(len(primes)):
        for j in range(len(primes)):
            table[i, j] = primes[i] * primes[j]
    return table