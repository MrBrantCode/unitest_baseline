"""
QUESTION:
Write a function `multiply_arrays` that takes two lists of integers `arr1` and `arr2` as input, and returns a new list where each element is the smallest prime number greater than 20. The function should ignore the actual product of the corresponding elements in the input arrays. The length of the output list should be the same as the length of the input arrays.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def multiply_arrays(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        product = arr1[i] * arr2[i]
        j = 21
        while not is_prime(j):
            j += 1
        result.append(j)
    return result