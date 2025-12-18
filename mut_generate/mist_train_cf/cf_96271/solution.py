"""
QUESTION:
Create a function `calculate_odd_prime_average` that calculates the average sum of all odd prime numbers in a given array. The function should return the average of the sum of odd prime numbers. The input array contains integers, and the function should handle arrays with zero or one odd prime number.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def calculate_odd_prime_average(arr):
    odd_prime_nums = [num for num in arr if num % 2 != 0 and is_prime(num)]
    if len(odd_prime_nums) == 0:
        return 0
    return sum(odd_prime_nums) / len(odd_prime_nums)