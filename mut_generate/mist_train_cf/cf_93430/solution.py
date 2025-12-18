"""
QUESTION:
Implement a function `reverse_string` that takes a string as input, removes all whitespace characters, and reverses the remaining characters. The function should handle both uppercase and lowercase characters and return the resulting string.
"""

def reverse_string(s):
    # Remove whitespace characters
    s = s.replace(" ", "")
    
    # Reverse the string in place
    s = s[::-1]
    
    return s