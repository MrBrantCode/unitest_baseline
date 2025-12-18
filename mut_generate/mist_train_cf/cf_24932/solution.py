"""
QUESTION:
Write a function `capitalize_words` that takes a list of strings as input and returns a new list where the first letter of each word in each string is capitalized, regardless of the original case.
"""

def capitalize_words(strings):
    return [' '.join(word.capitalize() for word in string.split()) for string in strings]