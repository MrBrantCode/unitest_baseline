"""
QUESTION:
Create a function called `reorder_string_alphabetically` that takes a string as input, ignores non-alphabetic characters, and returns the string with its words sorted in alphabetical order. The function should be case-sensitive.
"""

def reorder_string_alphabetically(target_string):
    """
    This function takes a string as input, ignores non-alphabetic characters, 
    and returns the string with its words sorted in alphabetical order.
    
    The function is case-sensitive. To make it case-insensitive, we can use 
    `str.lower` as a key in sorting.
    """
    # Remove symbols and convert string to a list of words
    words = target_string.split()
    words = [''.join(e for e in string if e.isalnum()) for string in words]
  
    # Sort list in Alphabetical order
    words.sort()
  
    # Join words back into a string
    result = ' '.join(words)
    return result