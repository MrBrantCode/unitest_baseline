"""
QUESTION:
Write a function `extract_word(transformed_word)` that takes a string `transformed_word` as input and returns the original word after removing the prefix "drove" and the suffix that follows the pattern "verb-noun". The function should assume that the prefix "drove" is always present and the suffix starts after the prefix.
"""

def extract_word(transformed_word):
    prefix = "drove"
    suffix = transformed_word[len(prefix):]
    original_word = suffix.split("-")[0]
    return original_word