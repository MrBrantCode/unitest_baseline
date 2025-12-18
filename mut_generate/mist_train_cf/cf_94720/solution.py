"""
QUESTION:
Write a function called `sum_of_primes` that calculates the sum of all prime numbers in a given array of integers. The function should return 0 if the input array is empty or if there are no prime numbers in the array.
"""

import math

def sum_of_primes(array):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    sum = 0
    for num in array:
        if is_prime(num):
            sum += num
    return sum