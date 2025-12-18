"""
QUESTION:
Create a function named `sum_of_prime_squares` that takes an integer `input_num` as input and returns the sum of the squares of all prime numbers between 1 and `input_num` (inclusive), excluding any multiples of 3 and perfect cubes.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect_cube(num):
    cube_root = round(num ** (1/3))
    return cube_root ** 3 == num

def sum_of_prime_squares(input_num):
    sum_of_squares = 0
    for num in range(1, input_num + 1):
        if is_prime(num) and num % 3 != 0 and not is_perfect_cube(num):
            sum_of_squares += num ** 2
    return sum_of_squares