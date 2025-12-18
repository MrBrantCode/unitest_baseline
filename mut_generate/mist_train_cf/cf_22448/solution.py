"""
QUESTION:
Write a function called `reverse_alphanumeric` that takes an input string, removes all non-alphanumeric characters, and returns the remaining alphanumeric characters in reverse order, ignoring case sensitivity. The function should use constant extra space and have a time complexity of O(n), where n is the length of the input string.
"""

def reverse_alphanumeric(input_string):
    alphanumeric = ""
    for char in input_string:
        if char.isalnum():
            alphanumeric += char.lower()
    return alphanumeric[::-1]