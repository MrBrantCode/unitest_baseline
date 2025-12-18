"""
QUESTION:
Create a function named `reverse_string` that takes a string `s` of maximum 100 alphanumeric characters as a parameter and returns the reversed string using recursion.
"""

def reverse_string(s):
    # Base case: if the string is empty or has only one character, return the string itself
    if len(s) <= 1:
        return s

    # Recursive case: reverse the substring excluding the first character, and concatenate it with the first character
    return reverse_string(s[1:]) + s[0]