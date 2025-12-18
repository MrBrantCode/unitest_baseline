"""
QUESTION:
Write a function `max_consecutive_prime_sum(nums)` that takes a list of integers `nums` as input and returns the largest sum of any two consecutive integers in the list that is a prime number. If no such prime sum exists, return -1.
"""

import math

def max_consecutive_prime_sum(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    max_sum = -1
    for i, j in zip(nums, nums[1:]):
        current_sum = i + j
        if is_prime(current_sum) and current_sum > max_sum:
            max_sum = current_sum
    return max_sum