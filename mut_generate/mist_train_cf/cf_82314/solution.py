"""
QUESTION:
Write a function called `reverse_string_order` that takes a string of words as input and returns the string with the order of words reversed. The function should split the input string into words, reverse their order, and then combine them back into a string. The words should be separated by spaces in the output string.
"""

def reverse_string_order(s):
    words = s.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence