"""
QUESTION:
Write a function `capitalizeWords` that takes a string of alphabetical characters separated by single spaces and returns a new string with each word capitalized. The input string only contains letters and spaces.
"""

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())