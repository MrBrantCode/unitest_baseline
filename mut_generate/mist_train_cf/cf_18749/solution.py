"""
QUESTION:
Write a function `check_strings` that takes a list of strings as input and returns `True` if any string in the list starts with 't' and ends with 'd', and the length of that string is a prime number. If no such string exists, the function should return `False`. The prime number check should only be performed for strings that start with 't' and end with 'd'.
"""

import math

def check_strings(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    for word in lst:
        if word.startswith("t") and word.endswith("d") and is_prime(len(word)):
            return True
    return False