"""
QUESTION:
Write a function `print_pairs(n)` that takes a positive integer `n` as input and prints all pairs of positive integers `(i, j)` such that `i + j` equals `n`. The pairs should be printed in increasing order of `i`. If `n` is a prime number, the function should print "No pairs exist for prime numbers." and return. If `n` is a perfect square, the function should print "Only one pair exists: (`sqrt(n)`, `sqrt(n)`)" and return.
"""

import math

def print_pairs(n):
    # Check if n is a prime number
    if is_prime(n):
        print("No pairs exist for prime numbers.")
        return
    
    # Check if n is a perfect square
    if is_perfect_square(n):
        sqrt_n = int(math.sqrt(n))
        print("Only one pair exists: ({}, {})".format(sqrt_n, sqrt_n))
        return
    
    # Generate pairs
    for i in range(1, n):
        j = n - i
        print("({}, {})".format(i, j))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect_square(num):
    sqrt_n = math.isqrt(num)
    return sqrt_n * sqrt_n == num