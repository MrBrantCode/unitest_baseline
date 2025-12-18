"""
QUESTION:
Write a function `reverse_words` that takes a string as input and returns the string with the order of words reversed, without using any built-in string manipulation functions and maintaining constant space complexity.
"""

def reverse_words(string):
    chars = list(string)
    reverse_string(chars, 0, len(chars) - 1)
    start = 0
    end = 0
    while end < len(chars):
        if chars[end] == ' ':
            reverse_string(chars, start, end - 1)
            start = end + 1
        end += 1
    reverse_string(chars, start, end - 1)
    return ''.join(chars)

def reverse_string(chars, start, end):
    while start < end:
        chars[start], chars[end] = chars[end], chars[start]
        start += 1
        end -= 1