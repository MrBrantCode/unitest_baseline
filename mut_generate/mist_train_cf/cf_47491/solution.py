"""
QUESTION:
Transform each word in a given list so that the last character is capitalized and all other characters are in lowercase. The function should handle special characters and punctuation marks correctly.

Create a function `transform(words)` that takes a list of strings as input and returns a new list of strings with the specified transformation applied to each word.
"""

def transform(words):
    transformed = []
    for word in words:
        new_word = word[:-1].lower() + word[-1].upper()
        transformed.append(new_word)
    return transformed