"""
QUESTION:
Create a function called `reverse_string` that takes a string `s` as a parameter, reverses it using recursion, and returns the reversed string. The input string will always be alphanumeric and can have a maximum length of 100 characters.
"""

def reverse_string(s):
    # Base case: if the string is empty or has only one character, return the string itself
    if len(s) <= 1:
        return s

    # Recursive case: reverse the substring excluding the first character, and concatenate it with the first character
    return reverse_string(s[1:]) + s[0]