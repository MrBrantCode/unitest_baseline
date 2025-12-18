"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` as input and returns the reversed string without using any built-in string reversal functions. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def reverse_string(s):
    s = list(s)
    start = 0
    end = len(s) - 1

    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    return ''.join(s)