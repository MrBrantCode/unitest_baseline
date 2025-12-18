"""
QUESTION:
Write a function named `reverse_string_words` that takes a string as input and returns the string with the order of words reversed. The function should be implemented in Python and should not use any external libraries or built-in functions other than the basic string and list methods.
"""

def reverse_string_words(s):
    words = s.split()
    words.reverse()
    return ' '.join(words)