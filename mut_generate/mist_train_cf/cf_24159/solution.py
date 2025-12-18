"""
QUESTION:
Write a function called 'reverse_words_order' that takes a string of two words as input, reverses the order of the words and returns the resulting string.
"""

def reverse_words_order(s):
    return ' '.join(s.split()[::-1])