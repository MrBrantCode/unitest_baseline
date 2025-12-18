"""
QUESTION:
Create a function called `printPrimes` that takes two integers `start` and `end` as input and uses a recursive approach to print out the prime numbers between `start` and `end` in an increasing order.
"""

import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def printPrimes(start, end):
    if start > end:
        return
    if isPrime(start):
        print(start)
    printPrimes(start + 1, end)