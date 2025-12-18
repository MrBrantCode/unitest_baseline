"""
QUESTION:
Write a function `invert_lexemes` that takes a line of text as input from the user, reverses each word in the text while preserving the original order of the words, and prints the modified text.
"""

def invert_lexemes(text):
    words = text.split(' ')
    inverted_words = [word[::-1] for word in words]
    inverted_text = ' '.join(inverted_words)
    return inverted_text