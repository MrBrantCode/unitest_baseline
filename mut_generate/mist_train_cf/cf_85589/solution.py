"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the reversed string without using any built-in reversing functions or libraries. The reversed string should retain the original capitalization and punctuation.
"""

def reverse_string(original_string):
    reversed_string = ''
    for i in original_string:
        reversed_string = i + reversed_string
    return reversed_string