"""
QUESTION:
Write a function `count_vowels` that takes a string as input, reads characters until a whitespace is encountered, and returns the count of vowels in the read characters. The function should be case-insensitive when counting vowels.
"""

def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char == ' ':
            break
        if char.lower() in vowels:
            count += 1
    return count