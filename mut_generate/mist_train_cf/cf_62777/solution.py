"""
QUESTION:
Write a function `reverse_unique` that takes a string `s` as input and returns a string with the same characters in reverse order, keeping only the first occurrence of any repeated character in the reversed string.
"""

def reverse_unique(s):
    s_rev = s[::-1]
    result = ''
    for ch in s_rev:
        if ch not in result:
            result += ch
    return result