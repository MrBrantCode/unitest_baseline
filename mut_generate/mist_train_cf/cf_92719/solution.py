"""
QUESTION:
Write a function named `next_prime` that takes an integer `number` as input and returns the smallest prime number greater than `number`. A prime number is an integer greater than 1 which is not divisible by any other numbers, except for 1 and itself. The function should also return a boolean indicating whether the input `number` is prime or not.
"""

import math

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

def next_prime(number):
    is_num_prime = is_prime(number)
    next_num = number
    while True:
        next_num += 1
        if is_prime(next_num):
            return next_num, is_num_prime