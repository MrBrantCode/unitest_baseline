"""
QUESTION:
Write a function `vowels_count` that takes a string as input and returns the number of vowels in the string. 'y' is considered a vowel only when it appears at the end of the word. The function should be case-insensitive and handle strings containing special characters, numbers, spaces, and empty strings without error.
"""

def vowels_count(s):
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels) + (1 if s.lower().endswith('y') else 0)