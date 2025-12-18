"""
QUESTION:
Construct a function named `construct_prime_composite` that takes a list of integers as input and returns two lists: one containing prime numbers and the other containing composite numbers. The function should optimize performance by only checking divisibility up to the square root of each number.
"""

import math

def construct_prime_composite(input_list):
    prime_numbers = []
    composite_numbers = []

    for num in input_list:
        if num > 1: 
            for i in range(2, math.isqrt(num) + 1):
                if (num % i) == 0:
                    composite_numbers.append(num)
                    break
            else:
                prime_numbers.append(num)
        else:
            composite_numbers.append(num)

    return prime_numbers, composite_numbers