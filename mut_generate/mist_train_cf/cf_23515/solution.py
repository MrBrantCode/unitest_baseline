"""
QUESTION:
Create a function named `first_letters` that takes a string as input and returns a string containing the first letter of each word. The words are separated by spaces.
"""

def first_letters(string):
    words = string.split()
    return "".join(word[0] for word in words)