"""
QUESTION:
Write a function named `reverse_words_order` that takes a string of words as input and returns a string with the words in reverse order, while maintaining the sequence of characters within each word. The input string contains only spaces as word separators. The output string should also use a single space as the word separator.
"""

def reverse_words_order(s):
    words = s.split(' ')
    reversed_words = words[::-1]
    return ' '.join(reversed_words)