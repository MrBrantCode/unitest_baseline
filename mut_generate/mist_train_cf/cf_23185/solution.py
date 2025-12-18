"""
QUESTION:
Given an array of integers, write a function `find_combinations(nums)` to print all unique combinations of the array that include at least three elements and have a sum that is both a prime number and a palindrome.
"""

import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_combinations(nums):
    combinations = []
    for r in range(3, len(nums) + 1):
        for combination in itertools.combinations(nums, r):
            if is_prime(sum(combination)) and is_palindrome(sum(combination)):
                combinations.append(combination)
    return combinations