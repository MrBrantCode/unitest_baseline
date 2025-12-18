"""
QUESTION:
Create a function called `extract_word` that takes a transformed word as a string input and returns the original word. The transformed word always starts with the prefix "drove" and ends with a suffix in the pattern "verb-noun". The function should remove the prefix and suffix from the input string to extract the original word.
"""

def extract_word(transformed_word):
    prefix = "drove"
    suffix = transformed_word[len(prefix):]
    original_word = suffix.split("-")[0]
    return original_word