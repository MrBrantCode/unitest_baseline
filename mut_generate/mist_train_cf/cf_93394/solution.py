"""
QUESTION:
Create a function `extract_unique_chars` that takes a string as input and returns a list containing the first and last occurring unique characters from the string in sorted order. The function should handle the case where there are no unique characters in the string.
"""

def extract_unique_chars(s):
    """
    Extracts the first and last occurring unique characters from a string and returns them in sorted order.

    Args:
        s (str): The input string.

    Returns:
        list: A list containing the first and last unique characters, or None if there are no unique characters.
    """
    unique_chars = []
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is unique and hasn't been added to the list yet
        if s.count(char) == 1 and char not in unique_chars:
            unique_chars.append(char)
    
    # Sort the unique characters list
    unique_chars.sort()
    
    # Return the first and last characters
    if unique_chars:
        return [unique_chars[0], unique_chars[-1]]
    else:
        return None