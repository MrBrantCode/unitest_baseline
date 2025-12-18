"""
QUESTION:
Write a function `sum_divisible_elements` that takes an array `arr` and a number `num` as input. The function should return the sum of all elements in the array that are divisible by `num` and greater than 10. The array must have a minimum length of 10, and `num` must be a prime number. Additionally, only consider elements in the array that are greater than the square root of `num`. If the array length is less than 10 or `num` is not prime, return an error message.
"""

import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def sum_divisible_elements(arr, num):
    if len(arr) < 10:
        return "Array length should be at least 10"
    if not is_prime(num):
        return "Given number is not prime"
    sqrt_num = math.sqrt(num)
    divisible_elements = [x for x in arr if x > 10 and x % num == 0 and x > sqrt_num]
    return sum(divisible_elements)