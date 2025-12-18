"""
QUESTION:
Implement the function `printPrimeNumbers(arr)` that prints the prime numbers in the given array `arr` in ascending order. The function should run in O(n) time complexity and use only constant extra space.
"""

import math

def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

def printPrimeNumbers(arr):
    for num in sorted(arr):
        if isPrime(num):
            print(num)