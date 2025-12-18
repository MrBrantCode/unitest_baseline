"""
QUESTION:
Write a function named `reverse_alphanumeric` that takes an input string as a parameter. The function should remove all non-alphanumeric characters from the string, ignore case sensitivity, and return the remaining alphanumeric characters in reverse order. The function should use constant extra space and have a time complexity of O(n), where n is the length of the input string. The input string will contain at least one alphanumeric character and will not be longer than 10^6 characters.
"""

def entance(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Reverse the alphanumeric string
    s = s[::-1]
    
    return s