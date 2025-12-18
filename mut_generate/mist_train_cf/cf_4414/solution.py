"""
QUESTION:
Write a recursive function named `prime_sum_recursive` that takes an integer `n` as input and returns the sum of all prime numbers between 1 and `n`. The function should only use iterative methods to check for prime numbers and should not use any built-in prime number checking functions or libraries. If the input number `n` is less than or equal to 1, the function should return -1. The function should handle large input numbers efficiently and optimize the iterative method to check for prime numbers without using any additional data structures or arrays.
"""

def is_prime(n, divisor=2):
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)

def prime_sum_recursive(n):
    if n <= 1:
        return -1
    elif n == 2:
        return 2
    elif is_prime(n):
        return n + prime_sum_recursive(n - 1)
    else:
        return prime_sum_recursive(n - 1)