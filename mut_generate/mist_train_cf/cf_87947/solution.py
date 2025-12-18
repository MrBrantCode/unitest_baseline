"""
QUESTION:
Write a function `is_prime_string(string)` that takes a string as input and returns True if the string consists only of digits, does not have leading zeros, and represents a prime number. The function should have a time complexity of O(n), where n is the length of the input string.
"""

import math

def is_prime_string(string):
    if len(string) == 0 or string[0] == '0':
        return False
    for char in string:
        if not char.isdigit():
            return False
    num = int(string)
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True