"""
QUESTION:
Write a function named `string_length` that calculates the length of a given string without using any built-in length function, ensuring it accurately handles Unicode characters. The input string can contain any combination of ASCII and Unicode characters.
"""

def string_length(text):
    counter = 0
    for i in text:
        counter += 1
    return counter