"""
QUESTION:
Write a recursive function `recursive_prime_sum(start, end)` that calculates the sum of all prime numbers within a given range from `start` to `end` (inclusive) after multiplying each prime number by 2. Implement a helper function `is_prime(n)` to check if a number `n` is prime or not. The recursive function should process a maximum of 100 prime numbers in each recursive call.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def recursive_prime_sum(start, end):
    if start > end:
        return 0

    sum_prime = 0
    for i in range(start, min(start + 100, end + 1)):
        if is_prime(i):
            sum_prime += (i * 2)

    return sum_prime + recursive_prime_sum(start + 100, end)