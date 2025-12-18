"""
QUESTION:
Write a function named `reverse_string` that takes an input string as a parameter and returns the reversed string without using built-in string reversal functions or methods, loops, or recursion. The function should work with any printable ASCII characters.
"""

def reverse_string(input_string):
    # Using string slicing to reverse the input string
    return input_string[::-1]