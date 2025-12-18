"""
QUESTION:
Write a function `printPrimesInReverse(arr)` that prints all prime numbers in the given array `arr` in reverse order. The function should use a helper function `isPrime(num)` to check if a number is prime. The `isPrime(num)` function should return `True` if the number is prime and `False` otherwise. The function `printPrimesInReverse(arr)` should not return anything, it should only print the prime numbers in reverse order.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_reverse(arr):
    for num in reversed(arr):
        if is_prime(num):
            print(num)