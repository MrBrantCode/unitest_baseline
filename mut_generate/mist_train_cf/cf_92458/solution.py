"""
QUESTION:
Write a function called `reverse_words` that takes a string as input and returns a string where each word in the input string is reversed. The input string may contain multiple words separated by spaces, and the output string should also have the words separated by spaces.
"""

def reverse_words(s):
    return ' '.join(word[::-1] for word in s.split())