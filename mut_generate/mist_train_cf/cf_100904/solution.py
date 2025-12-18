"""
QUESTION:
Create a function called `extract_word` that takes a string as input and returns the string with the prefix "drove" and a suffix in the pattern "verb-noun" (e.g., "walk-noun", "jump-noun") removed. The function should return the remaining word (e.g., "walk", "jump").
"""

def extract_word(transformed_word):
    prefix = "drove"
    suffix = transformed_word[len(prefix):]
    original_word = suffix.split("-")[0]
    return original_word