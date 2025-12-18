"""
QUESTION:
Write a function named `find_divisible_elements` that takes two parameters: an array `arr` and a number `num`. The function should return the sum of all elements in `arr` that are divisible by `num`, greater than 10, and greater than the square root of `num`. The function should only consider the array if it has a minimum length of 10 and if `num` is a prime number. The function should handle cases where the array contains negative numbers and zeros.
"""

import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_divisible_elements(arr, num):
    if len(arr) < 10:
        return "Array length should be at least 10."
    
    if not is_prime(num):
        return "Given number is not prime."
    
    sqrt_num = math.sqrt(num)
    divisible_sum = 0
    
    for element in arr:
        if element > sqrt_num and element > 10 and element % num == 0:
            divisible_sum += element
    
    return divisible_sum