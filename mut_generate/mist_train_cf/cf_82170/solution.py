"""
QUESTION:
Design a function named `primeQuad` that takes two parameters `s` and `e` representing a range of numbers, and prints all prime quadruplets within this range that satisfy the following conditions:

- The quadruplets are in quadratic progression (i.e., second differences of the series are constant).
- The total sum of the quadruplet is also a prime number.

The function should also include a helper function named `isPrime` to check if a number is prime.

The function should be optimized for time and space complexity, and should be able to handle large ranges efficiently.
"""

import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def primeQuad(s, e):
    primes = [i for i in range(s, e+1) if isPrime(i)]
    for i in range(len(primes)-3):
        if primes[i+1]-primes[i] == 2 and primes[i+2]-primes[i] == 6 and primes[i+3]-primes[i] == 8:
            if isPrime(sum(primes[i:i+4])):
                print(primes[i:i+4])