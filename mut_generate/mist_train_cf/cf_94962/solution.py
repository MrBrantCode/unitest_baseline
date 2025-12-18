"""
QUESTION:
Write a function `find_first_prime(arr)` that takes an array of integers as input and returns the first prime number in the array. The array can contain up to 10^6 elements, and the numbers in the array can range from 1 to 10^9. If no prime number is found, return None.
"""

import math

def find_first_prime(arr):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    for num in arr:
        if is_prime(num):
            return num
    return None