"""
QUESTION:
Write a function called `find_sum_of_prime_fibonacci_numbers` that takes two parameters `m` and `n`, both of which are positive integers where `m < n`. The function should return the sum of all prime numbers that can be expressed as the sum of two consecutive Fibonacci numbers in the range from `m` to `n` inclusive. 

Note that a Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_sum_of_prime_fibonacci_numbers(m, n):
    a, b = 0, 1
    prime_sum = 0
    while b <= n:
        if a + b >= m and is_prime(a + b):
            prime_sum += a + b
        a, b = b, a + b
    return prime_sum