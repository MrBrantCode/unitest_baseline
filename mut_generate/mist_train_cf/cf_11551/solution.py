"""
QUESTION:
Write a function `prime_divisor_sums` that takes in three arrays `arr1`, `arr2`, and `arr3` as input and returns a list of tuples, where each tuple contains a prime number and the sum of its divisors. The list should be sorted in descending order by the sum of divisors. The function should first classify each array element as a prime number or not, then for each prime number, find the sum of all its divisors, and finally sort the prime numbers based on the sum of their divisors.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

def prime_divisor_sums(arr1, arr2, arr3):
    prime_numbers = [num for num in arr1 + arr2 + arr3 if is_prime(num)]
    prime_sums = {prime: sum_divisors(prime) for prime in prime_numbers}
    return sorted(prime_sums.items(), key=lambda x: x[1], reverse=True)