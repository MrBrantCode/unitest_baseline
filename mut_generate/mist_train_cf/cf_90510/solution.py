"""
QUESTION:
Write a function named `smallest_prime_divisible` that takes an array of at least two positive integers as input and returns the smallest positive integer that is divisible by all numbers in the array and is a prime number. The function should have a time complexity of O(n), where n is the number of elements in the input array, and a space complexity of O(1), meaning it should not use any additional data structures.
"""

import math

def smallest_prime_divisible(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    result = nums[0]
    for i in range(1, len(nums)):
        result = (result * nums[i]) // math.gcd(result, nums[i])
    
    while not is_prime(result):
        result += 1
    
    return result