"""
QUESTION:
Create a function `repeat_characters` that takes a string `string` and an integer `n` as input. The function should return a string where each unique character in the input string is repeated `n` times, with duplicate characters removed. The order of the characters in the output string should be preserved based on their first occurrence in the input string.
"""

def repeat_characters(string, n):
    seen = set()
    repeated_chars = ''
    for char in string:
        if char not in seen:
            repeated_chars += char * n
            seen.add(char)
    return repeated_chars