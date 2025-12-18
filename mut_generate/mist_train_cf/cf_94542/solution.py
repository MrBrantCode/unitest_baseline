"""
QUESTION:
Create a function `reverse_string(s)` that takes a string `s` as input and returns the reversed string. The function should have a time complexity of O(n), where n is the length of the string, and use a constant amount of extra space. The function should also handle strings containing Unicode characters properly.
"""

def reverse_string(s):
    chars = list(s)
    length = len(chars)
    for i in range(length // 2):
        chars[i], chars[length - i - 1] = chars[length - i - 1], chars[i]
    return ''.join(chars)