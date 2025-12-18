"""
QUESTION:
Write a function called `find_max_prime_with_repeated_digit` that takes an array of integers as input and returns the maximum prime number in the array that has at least one repeated digit and the sum of its digits is divisible by 3. If no such number exists, return -1.
"""

import math

def find_max_prime_with_repeated_digit(arr):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = -1
    for num in arr:
        if is_prime(num) and len(set(str(num))) < len(str(num)) and sum(int(digit) for digit in str(num)) % 3 == 0:
            max_prime = max(max_prime, num)
    return max_prime