"""
QUESTION:
Create a function called `reverse_string` that takes a string `s` as input and returns the string in reverse order. The function must have a time complexity of O(n), where n is the length of the string, and use a constant amount of extra space. The function should also handle strings containing unicode characters properly.
"""

def reverse_string(s):
    chars = list(s)
    length = len(chars)
    for i in range(length // 2):
        chars[i], chars[length - i - 1] = chars[length - i - 1], chars[i]
    return ''.join(chars)