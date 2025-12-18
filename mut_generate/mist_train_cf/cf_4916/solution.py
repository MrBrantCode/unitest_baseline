"""
QUESTION:
Write a function `count_primes` that takes an array of integers as input and returns a tuple containing the count of prime numbers and the sum of all prime numbers in the array. The function should ignore negative integers and consider them as invalid input. The time complexity of the solution should be less than or equal to O(n * sqrt(m)), where n is the length of the array and m is the largest integer in the array. The solution should not use any precomputed prime numbers or external libraries to check for primality.
"""

import math

def count_primes(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    prime_sum = 0
    for num in arr:
        if num >= 0 and is_prime(num):
            count += 1
            prime_sum += num
    return count, prime_sum