"""
QUESTION:
Write a function named `reverse_words` that takes a string as input, reverses each word in the string while keeping the order of the words intact, and returns the modified string.
"""

def reverse_words(string):
    return ' '.join(word[::-1] for word in string.split())