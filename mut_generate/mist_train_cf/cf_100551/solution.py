"""
QUESTION:
Create a function named `multiply_arrays` that takes two arrays of integers as input and returns an array where each element is the smallest prime number greater than 20. The input arrays are of the same length, and corresponding elements from the input arrays are used to calculate the index of the first prime number greater than 20, not the product of the elements themselves.
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