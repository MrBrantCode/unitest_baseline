"""
QUESTION:
Create a function named `sum_of_primes` that takes an array of integers as input and returns the sum of all the prime numbers in the array. The function should be able to handle negative numbers and have a time complexity of O(n), where n is the size of the input array.
"""

import math

def sum_of_primes(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    prime_sum = 0
    for num in arr:
        if is_prime(abs(num)):
            prime_sum += num
    return prime_sum