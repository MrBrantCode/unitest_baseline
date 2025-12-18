"""
QUESTION:
Write a function `highest_prime_palindrome` that takes a list of integers as input and returns the highest prime number that is also a palindrome in the list. A prime number is a number greater than 1 that can only be divided by 1 and itself without leaving a remainder. A palindrome number remains the same when its digits are reversed. If no prime palindrome exists in the list, return 0.
"""

import math

def highest_prime_palindrome(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def is_palindrome(num):
        num_str = str(num)
        return num_str == num_str[::-1]

    highest = 0
    for num in numbers:
        if is_prime(num) and is_palindrome(num):
            highest = max(highest, num)
    return highest