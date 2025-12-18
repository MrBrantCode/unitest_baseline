"""
QUESTION:
Write a function `count_unique_characters` that takes a string as input and returns a dictionary containing the count of each unique character in the string. Then, compare two input strings using the `count_unique_characters` function to determine which string has more unique characters and return a dictionary for each string containing the count of each unique character.
"""

def count_unique_characters(s):
    """
    This function takes a string as input and returns a dictionary containing the count of each unique character in the string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    dict: A dictionary containing the count of each unique character in the string.
    """
    character_count = {}
    for c in s:
        if c not in character_count:
            character_count[c] = 1
        else:
            character_count[c] += 1
    return character_count