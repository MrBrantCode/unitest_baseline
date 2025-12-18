"""
QUESTION:
Write a function called `reverse_and_flip` that takes a string as input and returns the reversed string with the case of each character flipped (lowercase to uppercase and vice versa). The function should use looping structures and cannot use built-in "reverse" or "swapcase" functions.
"""

def reverse_and_flip(string):
    reversed_string = ''
    for char in string:
        if char.isupper():
            char = char.lower()
        elif char.islower():
            char = char.upper()
        reversed_string = char + reversed_string
    return reversed_string