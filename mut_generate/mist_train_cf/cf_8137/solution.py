"""
QUESTION:
Write a function `capitalize_sentence` that takes a string as input, removes all punctuation, and capitalizes the first letter of each word, ignoring any numbers or special characters.
"""

def capitalize_sentence(s):
    s = ''.join(ch for ch in s if ch.isalnum() or ch.isspace())
    return ' '.join(word.capitalize() for word in s.split())