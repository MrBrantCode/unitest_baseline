"""
QUESTION:
Create a function called `normalize_array` that takes an array of at least two positive integers as input and returns the array normalized such that its sum equals the nearest prime number greater than the sum of the original array.
"""

import math

def normalize_array(arr):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    array_sum = sum(arr)
    nearest_prime = array_sum
    while not is_prime(nearest_prime):
        nearest_prime += 1
    normalization_factor = nearest_prime / array_sum
    normalized_array = [math.ceil(element * normalization_factor) for element in arr]
    return normalized_array