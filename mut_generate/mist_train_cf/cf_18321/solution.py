"""
QUESTION:
Write a function called `reverse_string` that takes a string as input and returns the string with each word and character reversed in place. The function should not use any built-in string manipulation functions or data structures. The input string only contains spaces and alphabets.
"""

def reverse_string(s):
    chars = list(s)
    def reverse_array(start, end):
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1

    reverse_array(0, len(chars) - 1)
    start = 0
    for i in range(len(chars)):
        if chars[i] == ' ':
            reverse_array(start, i - 1)
            start = i + 1
        elif i == len(chars) - 1:
            reverse_array(start, i)
    return ''.join(chars)