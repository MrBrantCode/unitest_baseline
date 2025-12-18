"""
QUESTION:
Write a function called `reverse_string` that takes a string `s` as input and returns the reversed string. The function should not use any built-in string manipulation functions or methods and should have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(s):
    if not s:
        return s

    chars = list(s)
    left = 0
    right = len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)