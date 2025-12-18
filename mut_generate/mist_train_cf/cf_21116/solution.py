"""
QUESTION:
Write a function called `reverse_string` that takes an input string and returns the reversed string without using any loop or recursion. The input string should be at least 10 characters long. The function should handle strings with special characters and unicode characters properly.
"""

def reverse_string(input_string):
    # Check if the input string is at least 10 characters long
    if len(input_string) < 10:
        return "Input string should be at least 10 characters long."
    
    # Reverse the string using slicing and return the result
    return input_string[::-1]