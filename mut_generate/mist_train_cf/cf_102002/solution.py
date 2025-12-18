"""
QUESTION:
Create a function named `sum_prime_numbers` that takes an array of integers as input. The function should return the sum of all prime numbers in the array. If the array is empty, the function should return 0. If the array contains only non-prime numbers, the function should return -1.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def sum_prime_numbers(arr):
    if len(arr) == 0:
        return 0
    sum_primes = 0
    has_prime = False
    for num in arr:
        if is_prime(num):
            sum_primes += num
            has_prime = True
    if not has_prime:
        return -1
    return sum_primes