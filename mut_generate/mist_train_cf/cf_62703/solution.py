"""
QUESTION:
Implement a function named `remove_primes` that takes a multidimensional array of integers as input and returns the array with all prime numbers removed. The function should be able to handle arrays of any depth. The time complexity of the solution should be less than O(n^2), where n is the total number of elements in the array.
"""

from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def remove_primes(arr):
    if isinstance(arr, int):
        return [] if is_prime(arr) else [arr]
    else:
        new_arr = []
        for i in arr:
            new_arr.extend(remove_primes(i))
        return new_arr