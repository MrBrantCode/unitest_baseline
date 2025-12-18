"""
QUESTION:
Write a function called `reverse_in_place` that takes a string as input and returns the reversed string. The function should not use any built-in string reversal methods or functions, should only use a single loop, and should not create any new variables or data structures beyond what is necessary to solve the problem. The function should handle special characters, whitespace, and uppercase/lowercase letters correctly and have a time complexity of O(n), where n is the length of the input string.
"""

def reverse_in_place(string):
    chars = list(string)
    length = len(chars)
    for i in range(length // 2):
        chars[i], chars[length - i - 1] = chars[length - i - 1], chars[i]
    return ''.join(chars)