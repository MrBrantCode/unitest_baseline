"""
QUESTION:
Write a function `reverse_string` that takes an input string as a parameter, reverses it without using any built-in string reversal functions or methods, loops, or recursion, and returns the reversed string. The input string can contain any printable ASCII characters.
"""

def reverse_string(input_string):
    # Using string slicing to reverse the input string
    reversed_string = input_string[::-1]
    return reversed_string