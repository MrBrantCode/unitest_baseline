"""
QUESTION:
Create a function named `contains_uv_consecutively` that takes a string as input and returns a boolean value indicating whether the string contains the letters "u" and "v" consecutively, regardless of case. The function should ignore the case of the input string.
"""

def contains_uv_consecutively(s):
    # Convert the string to lowercase for case-insensitive comparison
    s = s.lower()
    
    # Iterate through the string and check if "u" and "v" are consecutive
    for i in range(len(s) - 1):
        if s[i] == 'u' and s[i+1] == 'v':
            return True
    
    # If no consecutive "u" and "v" found, return False
    return False