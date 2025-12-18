"""
QUESTION:
Create a function called `edit_string` that takes a string as input, replaces all spaces with hyphens, removes all punctuation marks, converts the string to lowercase, and reverses it.
"""

import string

def edit_string(s):
    """
    Replaces all spaces with hyphens, removes all punctuation marks, 
    converts the string to lowercase, and reverses it.

    Args:
        s (str): The input string.

    Returns:
        str: The edited string.
    """
    # Remove punctuation marks
    s = s.translate(str.maketrans('', '', string.punctuation))
    
    # Replace spaces with hyphens
    s = s.replace(' ', '-')
    
    # Convert to lowercase
    s = s.lower()
    
    # Reverse the string
    s = s[::-1]
    
    return s