"""
QUESTION:
Write a function `swap_chars(s)` that takes a string `s` as input and returns the modified string where pairs of adjacent characters are swapped. If the total characters in the string are odd, the last character should be left untouched.
"""

def swap_chars(s):
    result = ''
    i = 0
    while i < len(s) - 1:
        result += s[i+1] + s[i]
        i += 2

    # If the string has an odd length, add the last character
    if len(s) % 2 != 0:
        result += s[-1]

    return result