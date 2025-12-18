"""
QUESTION:
Create a function named `extract_word` that takes a transformed word as input and returns the original word. The transformed word has a prefix "drove" and a suffix following the pattern "verb-noun". The function should remove the prefix and the suffix, and then return the original word. The suffix should be split at the "-" character and the part before the "-" should be returned as the original word.
"""

def extract_word(transformed_word):
    prefix = "drove"
    suffix = transformed_word[len(prefix):]
    original_word = suffix.split("-")[0]
    return original_word