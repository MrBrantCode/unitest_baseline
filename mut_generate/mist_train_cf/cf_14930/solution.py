"""
QUESTION:
Create a function called `filter_primes` that takes an array of integers as input. The function should return a new array containing only the prime numbers from the input array, considering the absolute value of each number. The function should not modify the original array and have a time complexity of O(n*sqrt(k)), where n is the length of the input array and k is the maximum number in the array.
"""

import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def filter_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(abs(num)):
            primes.append(num)
    return primes