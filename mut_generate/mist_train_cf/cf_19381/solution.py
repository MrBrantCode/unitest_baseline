"""
QUESTION:
Write a function called `get_max_prime_with_pattern` that takes an array of integers as input and returns the maximum prime number in the array where the sum of its digits is divisible by 3. If no such prime number exists, return -1.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_max_prime_with_pattern(arr):
    max_prime = -1
    for num in arr:
        if is_prime(num):
            digit_sum = sum(int(digit) for digit in str(num))
            if digit_sum % 3 == 0:
                max_prime = max(max_prime, num)
    return max_prime