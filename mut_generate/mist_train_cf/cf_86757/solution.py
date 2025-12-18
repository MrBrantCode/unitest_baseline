"""
QUESTION:
Write a function called `reverse_in_place` that takes a string as input, reverses it in place without creating any new variables or data structures, and returns the reversed string. The function should handle special characters, whitespace, and uppercase/lowercase letters correctly, and should have a time complexity of O(n), where n is the length of the input string.
"""

def reverse_in_place(string):
    chars = list(string)
    length = len(chars)
    for i in range(length // 2):
        chars[i], chars[length - i - 1] = chars[length - i - 1], chars[i]
    return ''.join(chars)