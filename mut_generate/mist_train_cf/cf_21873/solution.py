"""
QUESTION:
Create a function `delete_prime_chars(s)` that takes a string `s` as input, removes characters at prime numbered positions, and returns the modified string. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string. The function should consider the position of a character in the string as its index plus one (1-indexed).
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def delete_prime_chars(s):
    result = []
    for i in range(len(s)):
        if not is_prime(i+1):
            result.append(s[i])
    return ''.join(result)