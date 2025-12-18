"""
QUESTION:
Write a function `remove_duplicates` that takes a string as input, removes duplicated characters, and returns the result as a string sorted in descending order based on the ASCII values of the characters. The function should return a string.
"""

def remove_duplicates(string):
    """
    Removes duplicated characters from a string and returns the result as a string sorted in descending order based on the ASCII values of the characters.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The string with duplicates removed and sorted in descending order.
    """
    unique_chars = sorted(set(string), reverse=True, key=lambda x: ord(x))
    return "".join(unique_chars)