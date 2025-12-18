"""
QUESTION:
Write a function named `find_divisible_elements` that takes an array of integers and a number as input. The function should return the sum of all elements in the array that are greater than 10, divisible by the given number, and also greater than the square root of the given number. The array must have a minimum length of 10, and the given number must be prime. The function should handle cases where the array contains negative numbers and zeros.
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