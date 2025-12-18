"""
QUESTION:
Implement a function `find_indexes(s)` that takes a string `s` of alphanumeric symbols as input and returns a list of position indexes of decimal numerals (from '0' to '9') that are not at the start or end of the string and are surrounded by prime numbers on both sides. If no such numerals are found, return -1. The function should ignore non-numeric characters and handle multiple occurrences within the same string.
"""

def find_indexes(s):
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    digits = []
    indexes = []
    for i, c in enumerate(s):
        if c.isdigit():
            digits.append((i, int(c)))
    for i in range(1, len(digits)-1):
        if is_prime(digits[i-1][1]) and is_prime(digits[i+1][1]):
            indexes.append(digits[i][0])
    return indexes if len(indexes) > 0 else -1