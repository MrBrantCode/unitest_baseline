"""
QUESTION:
Write a function called `reverse_alphanumeric` that takes a string as input, removes all non-alphanumeric characters while ignoring case sensitivity, and returns the remaining alphanumeric characters in reverse order. The function should use constant extra space and have a time complexity of O(n), where n is the length of the input string.
"""

def entrance(input_string):
    alphanumeric_string = ''.join(c.lower() for c in input_string if c.isalnum())
    return alphanumeric_string[::-1]