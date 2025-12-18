"""
QUESTION:
Write a function named `inverse_reformatting` that takes a list of discrete lexical elements (words) as input, and returns the original text by joining these elements with a single space, preserving their sequential organization.
"""

def inverse_reformatting(formatted_text):
    original_text = ' '.join(formatted_text)
    return original_text