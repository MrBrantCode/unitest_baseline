"""
QUESTION:
Write a function `get_length` that calculates the length of a given string without using any built-in length functions. The function should take a string as input and return the number of characters in the string.
"""

def get_length(text):
    counter = 0
    for i in text:
        counter += 1
    return counter