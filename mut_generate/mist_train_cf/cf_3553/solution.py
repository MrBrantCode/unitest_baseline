"""
QUESTION:
Create a function `oddPrimeSum` that takes an array of integers as input and returns a tuple containing a boolean indicating whether the array contains an odd number of prime elements and the sum of the prime elements in the array. The function should handle arrays containing both positive and negative integers, and it should have a time complexity of O(n) or better.
"""

import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def oddPrimeSum(array):
    sum = 0
    count = 0

    for element in array:
        if element == 0:
            continue
        if isPrime(abs(element)):
            count += 1
            sum += element

    if count % 2 == 1:
        return True, sum
    else:
        return False, 0