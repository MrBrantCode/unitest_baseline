"""
QUESTION:
Create a function `filter_words(s, target)` that takes a string of words `s` and a target word `target` as input. The words in `s` may be separated by commas, spaces, or both. The function should return a list of words in the original order, excluding all occurrences of the target word.
"""

def filter_words(s, target):
    words = s.replace(',', '').split()
    return [word for word in words if word != target]