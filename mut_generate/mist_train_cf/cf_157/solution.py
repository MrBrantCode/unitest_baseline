"""
QUESTION:
Write a function `normalize_array(arr)` that takes an array of at least two positive integers as input, where each integer is in the range 1 to 10^9. The function should return a new array where each element in the input array is multiplied by a normalization factor such that the sum of all elements in the output array is the nearest prime number greater than the sum of all elements in the input array.
"""

import math

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

def normalize_array(arr):
    array_sum = sum(arr)
    nearest_prime = array_sum
    while not is_prime(nearest_prime):
        nearest_prime += 1
    normalization_factor = nearest_prime / array_sum
    return [math.ceil(element * normalization_factor) for element in arr]