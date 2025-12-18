"""
QUESTION:
Write a function called `get_character_at_index` that takes a string `st` and an integer `index` as input and returns the character at the specified index in the string. If the index is out of range, the function should return a custom error message "Index out of range."
"""

def get_character_at_index(st, index):
    """
    Returns the character at the specified index in the string.
    
    Args:
        st (str): The input string.
        index (int): The index of the character to be returned.
    
    Returns:
        str: The character at the specified index if it exists, otherwise "Index out of range."
    """
    try:
        return st[index]
    except IndexError:
        return "Index out of range."