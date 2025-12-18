"""
QUESTION:
Create a function named `filter_primes` that takes an array of integers as input and returns a new array containing only the prime numbers from the input array, including negative prime numbers as their absolute values. The function should not modify the original array and have a time complexity of O(n*sqrt(k)), where n is the length of the input array and k is the maximum number in the array.
"""

import math

def filter_primes(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for num in numbers:
        if is_prime(abs(num)):
            primes.append(num)
    return primes