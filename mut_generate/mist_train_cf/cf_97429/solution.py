"""
QUESTION:
Write a function named `sum_of_squares_of_prime_divisors` that takes a positive integer `n` as input and returns the sum of the squares of all prime divisors of `n`. A prime divisor is a divisor that is a prime number. The input number `n` is a positive integer.
"""

import math

def sum_of_squares_of_prime_divisors(n):
    sum_squares = 0
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = True
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                sum_squares += i**2
                
    # Check if n itself is prime
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        sum_squares += n**2
                
    return sum_squares