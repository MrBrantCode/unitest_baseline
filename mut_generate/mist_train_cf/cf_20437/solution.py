"""
QUESTION:
Create a function `reverse_string(s)` that takes a string `s` as input and returns the reversed string without using any built-in functions, data structures (such as arrays or lists), variables, or loops. The function should have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(s):
    # Base case: if the string is empty or has only one character, return it as is
    if len(s) <= 1:
        return s

    # Recursive case: reverse the substring excluding the first character, and append the first character to the end
    return reverse_string(s[1:]) + s[0]