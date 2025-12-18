"""
QUESTION:
Create a function named `reverse_concatenate` that takes an array of strings as input, concatenates the strings in order (including whitespace and special characters), and returns the reversed result. The function should handle empty strings and arrays with a single string, and be optimized for large inputs.
"""

def reverse_concatenate(arr):
    # Concatenate all the strings
    concat = ''.join(arr)
    # Reverse the resultant string
    reversed_string = concat[::-1]

    return reversed_string