"""
QUESTION:
Write a function `remove_consecutive_repeats` that takes a string of numeric characters as input and returns a string with all consecutive repeating digits removed.
"""

def remove_consecutive_repeats(s):
    result = ""
    for i in range(len(s)):
        if i == 0 or s[i] != s[i-1]:
            result += s[i]
    return result