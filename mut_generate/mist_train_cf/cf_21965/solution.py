"""
QUESTION:
Write a function `sum_of_primes_and_fibonacci(arr)` that calculates the sum of all prime numbers and Fibonacci numbers in the given array, excluding any negative numbers. The function should take an array of integers as input and return the sum as an integer.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

def sum_of_primes_and_fibonacci(arr):
    total_sum = 0
    for num in arr:
        if num > 0:
            if is_prime(num) or is_fibonacci(num):
                total_sum += num
    return total_sum