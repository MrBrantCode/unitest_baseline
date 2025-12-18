"""
QUESTION:
Write a function named `reverse_words` that takes a string of words as input, reverses the order of the words, and returns the resulting string. Each word should maintain its original characters, but the words should be in reverse order of their original appearance. The function should handle strings with any number of words.
"""

def reverse_words(string):
    # Split the string into a list of words
    words = string.split()

    # Reverse the order of the words
    reversed_words = words[::-1]

    # Join the reversed words back into a string
    reversed_string = ' '.join(reversed_words)

    return reversed_string