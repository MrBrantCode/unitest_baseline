"""
QUESTION:
Write a function called `largest_prime_number` that takes an array of integers as a parameter and returns the largest prime number in the array. The function should consider the absolute values of the numbers in the array, as the array can contain both positive and negative numbers. If no prime numbers are found in the array, the function should return a message indicating this.
"""

import math

def largest_prime_number(array):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    largest_prime = None
    for num in array:
        if is_prime(abs(num)):
            if largest_prime is None or abs(num) > largest_prime:
                largest_prime = abs(num)
    if largest_prime is None:
        return "There are no prime numbers in the array."
    else:
        return largest_prime