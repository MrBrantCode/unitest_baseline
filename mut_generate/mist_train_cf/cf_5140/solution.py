"""
QUESTION:
Implement a function `findLargestPrimeNumber(numbers)` that takes a list of integers as input and returns the largest prime number in the list. The function should have a time complexity of O(N) and a space complexity of O(1). The input list can contain up to 10^7 integers, and the integers in the list can range from 1 to 10^9.
"""

import math

def isPrime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    sqrt_n = int(math.sqrt(n))
    for i in range(5, sqrt_n + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def findLargestPrimeNumber(numbers, index=0, largest=0):
    if index == len(numbers):
        return largest
    
    if numbers[index] > largest and isPrime(numbers[index]):
        largest = numbers[index]
    
    return findLargestPrimeNumber(numbers, index + 1, largest)