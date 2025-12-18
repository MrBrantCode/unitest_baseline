"""
QUESTION:
Create a function named `reverse_words` that takes a string of words as input, reverses the order of the words, and returns the result. The individual words themselves should not be reversed, only their order in the string. The input string is separated by spaces, and the output string should also be separated by spaces.
"""

def reverse_words(string):
    # Split the string into a list of words
    words = string.split()

    # Reverse the order of the words
    reversed_words = words[::-1]

    # Join the reversed words back into a string
    reversed_string = ' '.join(reversed_words)

    return reversed_string