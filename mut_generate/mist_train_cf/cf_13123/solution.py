"""
QUESTION:
Write a function named `is_prime()` and a main function to add up all the odd prime numbers in a given array. The `is_prime()` function should check if a number is prime. The main function should take an array of integers as input and return the sum of all odd prime numbers in the array. The function should handle arrays with any number of integers.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sum_odd_primes(arr):
    total = 0
    for num in arr:
        if num % 2 != 0 and is_prime(num):
            total += num
    return total