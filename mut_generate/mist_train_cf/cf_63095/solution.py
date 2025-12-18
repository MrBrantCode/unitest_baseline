"""
QUESTION:
Write a function named `filter_words` that takes two parameters, a string of words `s` separated by commas, spaces, or a combination of both, and a target word. The function should return a list of words from `s` in their original sequence with all occurrences of the target word removed.
"""

def filter_words(s, target):
    words = s.replace(',', '').split()  # Remove commas and split into words
    return [word for word in words if word != target]