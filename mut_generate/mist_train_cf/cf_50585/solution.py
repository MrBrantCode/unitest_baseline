"""
QUESTION:
Write a function called `find_index` that takes a string and a character as input and returns the index of the first occurrence of the character within the string, considering a zero-based index. The function should raise an error if the character is not found in the string.
"""

def find_index(text, char):
    """
    Returns the index of the first occurrence of the character within the string.
    
    Args:
        text (str): The input string.
        char (str): The character to find.
    
    Returns:
        int: The index of the first occurrence of the character.
    
    Raises:
        ValueError: If the character is not found in the string.
    """
    return text.index(char)