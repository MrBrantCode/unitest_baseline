"""
QUESTION:
Write a function named `reverse_string` that takes a string as input and returns the input string reversed. The function should not use any built-in string reversal methods, but instead rely on string indexing and slicing to achieve the reversal.
"""

def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string