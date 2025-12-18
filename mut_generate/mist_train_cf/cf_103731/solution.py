"""
QUESTION:
Write a function `unique_chars(s1, s2)` that returns a new string containing the characters present in both `s1` and `s2`, ignoring any duplicates and case sensitivity.
"""

def entance(s1, s2):
    # Convert both strings to lowercase
    s1 = s1.lower()
    s2 = s2.lower()
    
    # Initialize an empty string to store the unique characters
    unique_chars = ""
    
    # Iterate over each character in s1
    for char in s1:
        # Check if the character is present in s2 and is not already in unique_chars
        if char in s2 and char not in unique_chars:
            unique_chars += char
    
    return unique_chars