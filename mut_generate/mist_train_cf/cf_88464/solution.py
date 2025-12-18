"""
QUESTION:
Write a recursive function named `prime_sum_recursive` that calculates the sum of all prime numbers between 1 and a given input number `n`. The function should return -1 if `n` is less than or equal to 1. 

The function should check for prime numbers iteratively without using any built-in prime number checking functions or libraries. It should not use any additional data structures or arrays to store prime numbers. The iterative method should be optimized to minimize the number of iterations required to determine if a number is prime.
"""

def prime_sum_recursive(n):
    def is_prime(num, divisor=2):
        if num < 2:
            return False
        if divisor * divisor > num:
            return True
        if num % divisor == 0:
            return False
        return is_prime(num, divisor + 1)

    if n <= 1:
        return -1
    elif n == 2:
        return 2
    elif is_prime(n):
        return n + prime_sum_recursive(n - 1)
    else:
        return prime_sum_recursive(n - 1)