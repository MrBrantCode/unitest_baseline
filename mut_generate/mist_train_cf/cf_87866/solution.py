"""
QUESTION:
Write a function named `capitalize_words` that takes a string as input, capitalizes the first character of each word, and returns the resulting string. The input string may contain punctuation marks.
"""

def capitalize_words(string):
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)