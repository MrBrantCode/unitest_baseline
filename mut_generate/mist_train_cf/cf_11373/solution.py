"""
QUESTION:
Create a function `hasOddPrimeElements(arr)` that determines whether the given array `arr` contains an odd number of prime elements. The array can contain both positive and negative integers. The function should return `True` if the array contains an odd number of prime elements and `False` otherwise. Note that the absolute value of a negative number should be considered when determining if it's a prime number. The function should also handle edge cases such as an empty array or an array with only one element.
"""

import math

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def entance(arr):
    if len(arr) == 0:
        return False
    count = 0
    for num in arr:
        if num < 0:
            num = abs(num)
        if num == 2 or num == 3:
            count += 1
        elif num > 3 and isPrime(num):
            count += 1
    return count % 2 == 1