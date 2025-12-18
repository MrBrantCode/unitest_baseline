"""
QUESTION:
Write a function named `reverse_words` that takes a string of words as input and returns a string where each word is reversed, maintaining the original word order. The input string contains only spaces and alphabetic characters.
"""

def reverse_words(s):
    return ' '.join(word[::-1] for word in s.split())