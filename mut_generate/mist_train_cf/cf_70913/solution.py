"""
QUESTION:
Write a function named `is_prime` that checks if a given number is prime. Use this function to find the 10001st prime number. A prime number is a natural number greater than 1 that is not a product of a positive integer other than 1 and itself. Note that the input number is not provided and the function should be able to handle any input number. The function should be able to efficiently check if a number is prime by only checking divisibility up to its square root.
"""

import math

def is_prime(num):
    if num <= 1: 
        return False
    if num == 2: 
        return True
    if num % 2 == 0: 
        return False
    sqr = math.sqrt(num)
    for divisor in range(3, int(sqr) + 1, 2):
        if num % divisor == 0:
            return False
    return True