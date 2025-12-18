"""
QUESTION:
Write a function `maintain_ordered_uppercase(text)` that accepts a string and returns a string containing only the uppercase letters from the input, in their original order. Ignore lowercase letters, numerals, punctuation marks, and whitespace characters.
"""

def maintain_ordered_uppercase(text):
    """
    maintain_ordered_uppercase is a function that accepts a string and returns a string in which only the uppercase letters are kept, while ensuring that their original sequence is maintained. Ignore lowercase letters, numerals, punctuation marks, and whitespace characters.
    """
    return ''.join(filter(str.isupper, text))