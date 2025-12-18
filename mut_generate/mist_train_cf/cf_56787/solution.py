"""
QUESTION:
Write a function `primeProduct(nums)` that takes a list of integers as input and returns a Boolean indicating whether the product of the numbers in the list is a prime number.
"""

from functools import reduce
from math import sqrt

def primeProduct(nums):
    def isPrime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    product = reduce((lambda x, y: x * y), nums)
    return isPrime(product)