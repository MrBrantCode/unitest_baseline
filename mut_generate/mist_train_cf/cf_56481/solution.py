"""
QUESTION:
Design a function named `sum_of_squares_of_primes(n)` to calculate the sum of the squares of the prime numbers between 1 and a given integer `n`. The function should take an integer `n` as input and return the sum of squares of all prime numbers within this range.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

def sum_of_squares_of_primes(n):
    sum_of_squares = 0
    for i in range(1, n + 1):
        if is_prime(i):
            sum_of_squares += i ** 2
    return sum_of_squares