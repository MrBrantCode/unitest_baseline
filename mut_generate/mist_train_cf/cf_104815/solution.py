"""
QUESTION:
Write a function `repeat_characters` that takes a string of lowercase alphabets and an integer `n` as input, and returns a string where each character in the input string is repeated `n` times. The input string will have at most 100 characters and `n` will be between 1 and 10.
"""

def repeat_characters(s, n):
    result = ""
    for char in s:
        result += char * n
    return result