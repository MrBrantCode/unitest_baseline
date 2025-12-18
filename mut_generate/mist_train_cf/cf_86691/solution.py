"""
QUESTION:
Create a recursive function `sum_of_squares` that takes an array of at most 100 positive integers as input and returns the sum of the squares of all prime numbers in the array, the number of prime numbers, the number of composite numbers, and a list of all prime numbers in ascending order.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_squares(arr):
    prime_sum = 0
    prime_count = 0
    composite_count = 0
    prime_nums = []

    for num in arr:
        if is_prime(num):
            prime_sum += num ** 2
            prime_count += 1
            prime_nums.append(num)
        else:
            composite_count += 1

    prime_nums.sort()

    return prime_sum, prime_count, composite_count, prime_nums