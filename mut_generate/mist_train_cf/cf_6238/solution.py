"""
QUESTION:
Write a function `largest_prime_number` that takes an array of numbers as input and returns the largest prime number in the array. If there are no prime numbers in the array, return -1.

The function must use a helper function `is_prime` that returns True if a number is prime and False otherwise. The `is_prime` function should have a time complexity of O(sqrt(num)) and use memoization to optimize the computation. The `is_prime` function should be implemented using a recursive approach is not required but is allowed. The overall time complexity of `largest_prime_number` should be O(n*sqrt(m)), where n is the length of the array and m is the largest number in the array.
"""

from math import isqrt

def largest_prime_number(numbers):
    def is_prime(num, memo={}):
        if num in memo:
            return memo[num]
        
        if num <= 1:
            memo[num] = False
            return False
        
        if num == 2:
            memo[num] = True
            return True
        
        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                memo[num] = False
                return False
        
        memo[num] = True
        return True
    
    largest_prime = -1
    for num in numbers:
        if is_prime(num) and num > largest_prime:
            largest_prime = num
    return largest_prime