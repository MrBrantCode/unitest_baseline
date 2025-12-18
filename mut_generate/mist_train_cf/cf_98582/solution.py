"""
QUESTION:
Write a Python function called `extract_word` that takes a string `transformed_word` as input and returns the word with "drove" prefix and the suffix after the first hyphen removed.
"""

def extract_word(transformed_word):
    prefix = "drove"
    suffix = transformed_word[len(prefix):]
    original_word = suffix.split("-")[0]
    return original_word