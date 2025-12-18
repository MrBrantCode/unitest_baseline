"""
QUESTION:
Write a function `find_prime_palindromes` that takes a list of integers as input and returns a list of integers that are both palindromes and prime numbers. The function should have a time complexity of O(n) and use only constant space, where n is the number of elements in the input list. The input list contains non-negative integers.
"""

import math

def find_prime_palindromes(nums):
    def is_palindrome(num):
        # Convert number to string for easy comparison
        num_str = str(num)
        # Check if the string is the same as its reverse
        return num_str == num_str[::-1]

    def is_prime(num):
        # 0 and 1 are not prime
        if num < 2:
            return False
        # Check if num is divisible by any number less than its square root
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    palindromes = []
    for num in nums:
        if is_palindrome(num) and is_prime(num):
            palindromes.append(num)
    return palindromes