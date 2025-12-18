"""
QUESTION:
Write a function `check_string(s, a=5, b=20)` that takes a string `s` and optional parameters `a` and `b` as input. The function should return a tuple containing a boolean indicating whether the string's length falls within the range `[a, b]` and the string contains at least three distinct characters, and a dictionary containing the frequency of each character in the string.
"""

def check_string(s, a=5, b=20):
    if not (a <= len(s) <= b):
        return False, {}

    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return len(char_counts) >= 3, char_counts