"""
QUESTION:
Write a function `largest_prime_number` that takes an array of integers as input and returns the largest prime number in the array. The function should consider the absolute value of each number in the array and ignore non-prime numbers. If the array does not contain any prime numbers, the function should return a message indicating this. The input array can contain both positive and negative integers.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_number(array):
    largest_prime = None
    for num in array:
        if is_prime(abs(num)):
            if largest_prime is None or abs(num) > largest_prime:
                largest_prime = abs(num)
    if largest_prime is None:
        return "There are no prime numbers in the array."
    else:
        return largest_prime