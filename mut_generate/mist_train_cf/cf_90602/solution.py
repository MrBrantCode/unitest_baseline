"""
QUESTION:
Write a function `recursive_prime_sum(start, end)` that calculates the sum of all prime numbers in the range from `start` to `end` (inclusive), with each prime number multiplied by 2. The function should use recursion to divide the range into sub-ranges of at most 100 prime numbers. You may also need to implement a helper function `is_prime(n)` to check if a number `n` is prime or not.
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