"""
QUESTION:
Write a function `longest_digit_substring` that takes a string as input and returns the longest substring containing only digits. If there are multiple substrings of the same maximum length, return the first one encountered. The input string may contain alphanumeric characters and special symbols.
"""

def longest_digit_substring(s):
    if not s:
        return ""

    max_length = 0
    max_substring = ""
    current_substring = ""

    for char in s:
        if char.isdigit():
            current_substring += char
            if len(current_substring) > max_length:
                max_length = len(current_substring)
                max_substring = current_substring
        else:
            current_substring = ""

    return max_substring