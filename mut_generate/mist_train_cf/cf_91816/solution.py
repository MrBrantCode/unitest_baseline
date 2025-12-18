"""
QUESTION:
Create a function `hasOddPrimeElements(arr)` that determines whether the given array `arr` contains an odd number of prime elements. The array can contain both positive and negative integers. The function should return `True` if the array has an odd number of prime elements and `False` otherwise.
"""

import math

def hasOddPrimeElements(arr):
    def is_prime(n):
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

    if len(arr) == 0:
        return False
    count = 0
    for num in arr:
        if num < 0:
            num = abs(num)
        if num == 2 or num == 3:
            count += 1
        elif num > 3 and is_prime(num):
            count += 1
    return count % 2 == 1