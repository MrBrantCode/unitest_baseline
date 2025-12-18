"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` as input and returns the reversed string without using any built-in functions or methods for reversing the string, and without using any additional data structures. The function should handle all UTF-8 valid characters and work with a string of any length, while also optimizing for high performance by minimizing space complexity.
"""

def reverse_string(s):
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)