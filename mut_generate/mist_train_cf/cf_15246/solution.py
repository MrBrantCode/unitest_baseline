"""
QUESTION:
Create a function named `normalize_array` that takes an array of integers as input, calculates the sum of all elements, finds the nearest prime number greater than the sum, and then adjusts the elements in the array such that their sum equals the nearest prime number. The adjustment is made by subtracting a uniform value from each element, which is the difference between the nearest prime number and the original sum divided by the length of the array. The function should return the normalized array. The array can contain any integer values, and the function should work for arrays of any length.
"""

import math

def normalize_array(arr):
    arr_sum = sum(arr)
    prime = arr_sum + 1
    while not is_prime(prime):
        prime += 1
    difference = prime - arr_sum
    return [x - (difference // len(arr)) for x in arr]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True