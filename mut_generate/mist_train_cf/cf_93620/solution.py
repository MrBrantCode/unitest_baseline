"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` as input and returns the reversed string without using built-in string reversal functions, slicing, or any additional data structures. The function should have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(s):
    # Base case: if the string is empty or has only one character, return the string itself
    if len(s) <= 1:
        return s
    
    # Recursive case: reverse the substring starting from the second character,
    # and concatenate the first character at the end
    return reverse_string(s[1:]) + s[0]