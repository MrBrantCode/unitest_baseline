"""
QUESTION:
Write a function `count_unique_characters` that takes a string input and returns the count of unique characters present in it. The input string must have at least 10 non-space characters and may contain uppercase characters, duplicate letters, and whitespace. The function should operate through a multi-step approach that includes preprocessing the input string to remove whitespace and convert all characters to lowercase, then count the unique characters using a set, and finally create a table that lists the input string and its corresponding unique character count.
"""

def count_unique_characters(string):
    """
    This function takes a string input, removes whitespace, converts to lowercase, 
    counts the unique characters and returns the count.

    Args:
    string (str): The input string.

    Returns:
    int: The count of unique characters.
    """
    # Preprocessing the input string
    string = string.replace(" ", "").lower()
    
    # Counting the unique characters
    unique_chars = set(string)
    unique_count = len(unique_chars)
    
    return unique_count