"""
QUESTION:
Write a function called `replace_second_smallest_prime` that takes an array of positive integers as input and replaces the second smallest prime number in the array with the sum of all prime numbers in the array. If the array contains less than two prime numbers, return -1.
"""

import math

def replace_second_smallest_prime(arr):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    prime_sum = 0
    primes = []

    for num in arr:
        if is_prime(num):
            prime_sum += num
            primes.append(num)

    if len(primes) < 2:
        return -1

    second_smallest = sorted(primes)[1]
    arr[arr.index(second_smallest)] = prime_sum

    return arr