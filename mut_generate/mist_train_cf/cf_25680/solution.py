"""
QUESTION:
Write a function `find_unique(string)` that takes a string as input and returns a list of all unique characters in the string. The function should ignore duplicate characters and maintain the original order of characters in the string.
"""

def find_unique(string): 
    """
    Returns a list of all unique characters in the string, 
    ignoring duplicates and maintaining the original order.

    Args:
        string (str): The input string.

    Returns:
        list: A list of unique characters.
    """
    uniq_char = [] 
    for i in string: 
        if i not in uniq_char: 
            uniq_char.append(i) 
    return uniq_char