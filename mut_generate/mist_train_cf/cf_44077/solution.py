"""
QUESTION:
Write a function `last_non_repeated_char` that takes an input string and returns the last non-repeated character in the string, considering case sensitivity. If all characters are repeated, return 'All are Repeated'.
"""

def last_non_repeated_char(input_string):
    char_count = {}
    for char in reversed(input_string):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in reversed(input_string):
        if char_count[char] == 1:
            return char
    return "All are Repeated"