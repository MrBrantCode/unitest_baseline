"""
QUESTION:
Write a function `concatenate_strings(string1, string2)` that takes two string arguments. The function should return a string that is the concatenation of `string1` and `string2`, but with the following conditions: the resulting string should be in alphabetical order, should not contain any duplicate characters, and should only consider alphabetical characters (ignoring special characters and numbers).
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