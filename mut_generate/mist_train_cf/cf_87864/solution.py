"""
QUESTION:
Design a function `concatenate_strings(string1, string2)` that takes two strings as input, concatenates them, removes special characters and numbers, converts to lowercase, sorts the string alphabetically, and removes duplicate characters. The function should only consider alphabetical characters and ignore any special characters or numbers in the input strings.
"""

def concatenate_strings(string1, string2):
    # Concatenate the strings
    result = string1 + string2
    
    # Remove special characters and numbers, and convert to lowercase
    result = ''.join([c.lower() for c in result if c.isalpha()])
    
    # Sort the string alphabetically
    result = ''.join(sorted(result))
    
    # Remove duplicate characters
    result = ''.join([c for i, c in enumerate(result) if c not in result[:i]])
    
    return result