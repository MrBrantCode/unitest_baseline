"""
QUESTION:
Write a function `printPrimeNumbers` that takes an array of integers as input and prints all prime numbers in the array in ascending order. The function should have a time complexity of O(n) and use only constant extra space.
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