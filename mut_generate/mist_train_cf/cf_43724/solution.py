"""
QUESTION:
Create a function `count_chars(s)` that accepts a character string `s` as an argument and returns a tuple containing the length of the string and a dictionary with the count of each character found within it.
"""

def count_chars(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return len(s), char_counts