"""
QUESTION:
Write a function `reverse_string(s)` that conducts an in-place reversal of a string `s` using Python, excluding special characters and numerals, while preserving their original positions and handling unicode characters. The function should return the modified string.
"""

def reverse_string(s):
    s = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalpha():
            left += 1
        elif not s[right].isalpha():
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return ''.join(s)