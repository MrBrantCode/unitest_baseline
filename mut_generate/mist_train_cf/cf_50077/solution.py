"""
QUESTION:
Write a function `reverse_words(input_text)` that takes a string of words as input, reverses each word individually, and returns the resulting string with the words in their original order. The input string may contain multiple words separated by spaces.
"""

def reverse_words(input_text):
    words = input_text.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)