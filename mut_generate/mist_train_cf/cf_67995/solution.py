"""
QUESTION:
Write a function named `first_palindrome` that takes a string as input and returns a tuple containing the first palindrome found in the string, its starting position (0-indexed), and its ending position (0-indexed, non-inclusive). If no palindrome is found, return `None` for all three elements. The function should be case-sensitive, and it should consider all substrings of the input string, starting with the longest one in decreasing order of length.
"""

def first_palindrome(string):
    length = len(string)
    for size in range(length, 0, -1):
        for start in range(length - size + 1):
            str_slice = string[start:start + size]
            if str_slice == str_slice[::-1]:
                return str_slice, start, start + size
    return None, None, None