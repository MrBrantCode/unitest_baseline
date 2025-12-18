"""
QUESTION:
Write a function `remove_vowels` that takes a string `input_string` as input and returns a string with all vowels removed. The function should handle both lowercase and uppercase vowels, remove any leading or trailing whitespace, and have a time complexity of O(n), where n is the length of the input string. Do not use built-in string manipulation functions or methods such as replace() or translate().
"""

def remove_vowels(input_string):
    return ''.join(char for char in input_string.strip() if char.lower() not in 'aeiou')