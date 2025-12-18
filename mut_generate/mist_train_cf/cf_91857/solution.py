"""
QUESTION:
Write a function named `reverse_words` that takes a string `input_str` as input, and returns the input string with the order of its words reversed. The function should split the input string into words, reverse the order of the words, and join the reversed words back into a single string with spaces as separators.
"""

def reverse_words(input_str):
    words = input_str.split()
    words.reverse()
    reversed_str = ' '.join(words)
    return reversed_str