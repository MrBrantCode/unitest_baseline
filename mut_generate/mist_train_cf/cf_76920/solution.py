"""
QUESTION:
Write a function `reverseString(s)` that takes an array of characters `s` as input and reverses the sequence of characters in-place while maintaining case sensitivity. The function should not allocate additional space and should handle special characters and numbers. The length of `s` is between 1 and 10^5 (inclusive) and `s[i]` is a printable ASCII character.
"""

def reverseString(s):
    start = 0
    end = len(s)-1
    while start <= end:
        s[start], s[end] = s[end], s[start]
        start = start + 1
        end = end - 1
    return s