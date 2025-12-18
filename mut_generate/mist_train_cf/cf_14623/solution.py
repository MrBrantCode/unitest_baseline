"""
QUESTION:
Write a function named `reverse_and_capitalize_words` that takes an array of strings as input. The function should reverse each word, capitalize the first letter of each reversed word, and return the resulting words as a comma-separated string.
"""

def reverse_and_capitalize_words(arr):
    return ", ".join([word[::-1].capitalize() for word in arr])