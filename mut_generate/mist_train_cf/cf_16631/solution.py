"""
QUESTION:
Reverse a string in place in groups of 2 characters, swapping the characters within each group, without using additional data structures or built-in functions, assuming the input string has an even number of characters. Implement this functionality in a function named `reverse_string`.
"""

def reverse_string(s):
    """
    Reverses a string in place in groups of 2 characters, 
    swapping the characters within each group.

    Args:
    s (str): The input string to be reversed.

    Returns:
    str: The reversed string.
    """
    # Convert string to list since strings are immutable
    s = list(s)
    
    # Iterate through the string in steps of 2
    for i in range(0, len(s), 2):
        # Swap the current character with the next character
        s[i], s[i+1] = s[i+1], s[i]
    
    # Convert list back to string
    return ''.join(s)