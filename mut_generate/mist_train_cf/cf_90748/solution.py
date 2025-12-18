"""
QUESTION:
Write a function named `reverse_words` that takes a string as input, reverses each word in the string while maintaining the original word order, and returns the resulting string. The function should be able to handle strings containing punctuation marks attached to words, and it should not remove or alter these marks.
"""

def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)