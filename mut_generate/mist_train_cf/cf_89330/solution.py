"""
QUESTION:
Find the largest prime number in an array of numbers. 

You need to implement a function called `largest_prime_number` that takes an array of numbers as input and returns the largest prime number in the array. If there are no prime numbers in the array, the function should return -1.

The function `largest_prime_number` should use a helper function `is_prime(num: int) -> bool` that returns True if a number is prime and False otherwise. The `is_prime` function should have a time complexity of O(sqrt(num)) and should use a recursive approach with memoization to optimize the computation.
"""

from math import isqrt

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

def largest_prime_number(numbers):
    largest_prime = -1
    for num in numbers:
        if is_prime(num) and num > largest_prime:
            largest_prime = num
    return largest_prime