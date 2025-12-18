"""
QUESTION:
Write a function named `sum_of_primes(numbers)` that calculates the total sum of all prime numbers in the given list of integers. The list may contain up to 1000 elements. You are not allowed to use any built-in functions or libraries to check for prime numbers.
"""

def is_prime(num):
    if num < 2:  # 0 and 1 are not prime
        return False
    for i in range(2, int(num**0.5) + 1):  # checking divisibility up to square root of num
        if num % i == 0:
            return False
    return True

def sum_of_primes(numbers):
    prime_sum = 0
    for num in numbers:
        if is_prime(num):
            prime_sum += num
    return prime_sum