"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the reversed string, ignoring any punctuation and whitespace characters. The function should not use any built-in string reversal functions or methods, and should only use basic string manipulation operations and loops. The input string may contain lowercase or uppercase alphabets, punctuation, whitespace characters, and digits.
"""

def reverse_string(string):
    # Remove punctuation and whitespace
    string = ''.join(char for char in string if char.isalpha())
    # Initialize an empty string to store the reversed string
    reversed_string = ''
    # Iterate through the characters in the string in reverse order
    for i in range(len(string)-1, -1, -1):
        # Add each character to the reversed string
        reversed_string += string[i]
    return reversed_string