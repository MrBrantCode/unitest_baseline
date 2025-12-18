"""
QUESTION:
Write a function named `extract_word` that takes a string as input and returns the original word by removing the prefix "drove" and the suffix that starts with a verb and ends with "-noun". The suffix should be split at the hyphen and the part before the hyphen should be discarded.
"""

def extract_word(transformed_word):
    prefix = "drove"
    suffix = transformed_word[len(prefix):]
    original_word = suffix.split("-")[0]
    return original_word