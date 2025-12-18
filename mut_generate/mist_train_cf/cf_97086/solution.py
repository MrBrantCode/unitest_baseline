"""
QUESTION:
Write a function called `reverse_alphanumeric` that takes an input string and returns its alphanumeric characters in reverse order, ignoring case sensitivity. The function should use constant extra space and have a time complexity of O(n), where n is the length of the input string.
"""

def reverse_alphanumeric(input_string):
    # Create an empty string to store the alphanumeric characters
    alphanumeric = ""
    
    # Iterate over each character in the input string
    for char in input_string:
        # Check if the character is alphanumeric
        if char.isalnum():
            # Append the lowercase version of the character to the alphanumeric string
            alphanumeric += char.lower()
    
    # Reverse the alphanumeric string using slicing
    reversed_alphanumeric = alphanumeric[::-1]
    
    return reversed_alphanumeric