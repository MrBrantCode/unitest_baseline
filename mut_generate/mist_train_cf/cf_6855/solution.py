"""
QUESTION:
Implement a function `print_prime_numbers(arr)` that takes an array of integers as input and prints the prime numbers in ascending order. The function should run in O(n) time complexity and use only constant extra space. It should handle large numbers up to 10^9 and correctly identify prime numbers among integers in the array, excluding non-integer values and non-positive numbers.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_prime_numbers(arr):
    prime_numbers = []
    for num in arr:
        if isinstance(num, int) and num > 0 and is_prime(num):
            prime_numbers.append(num)
    prime_numbers.sort()
    for num in prime_numbers:
        print(num)