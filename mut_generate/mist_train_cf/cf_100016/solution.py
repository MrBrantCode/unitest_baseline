"""
QUESTION:
Write a function called `extract_word` that takes a string as input, removes the prefix "drove" and the suffix "-noun" (where the word before the suffix can be any verb), and returns the original word. The function should be able to handle strings in the format "drivewalk-noun" or "drovejump-noun".
"""

def extract_word(transformed_word):
    prefix = "drove"
    suffix = transformed_word[len(prefix):]
    original_word = suffix.split("-")[0]
    return original_word