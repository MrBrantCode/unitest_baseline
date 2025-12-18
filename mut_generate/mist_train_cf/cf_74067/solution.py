"""
QUESTION:
Create a function named `find_nearest_prime` that finds the nearest prime number to a given integer. The function should take an integer `num` as input and return the nearest prime number. The function should check numbers on both sides of the input number, moving outward to find the closest prime.
"""

import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def find_nearest_prime(num):
    num1 = num - 1
    num2 = num + 1
    while True:
        if is_prime(num1):
            return num1
        if is_prime(num2):
            return num2
        num1 -= 1
        num2 += 1