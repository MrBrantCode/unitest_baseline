"""
QUESTION:
Write a function called `reverse_string` that takes a string as input and returns the reversed string without using any built-in reverse functions or slicing. The function should maintain the original case of the letters.
"""

def reverse_string(input_string):
    reversed_string = ''
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string