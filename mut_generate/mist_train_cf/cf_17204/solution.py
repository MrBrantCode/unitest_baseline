"""
QUESTION:
Write a function `count_characters` that takes a string as input and returns a dictionary where the keys are unique alphabetic characters in the string (ignoring case) and the values are the counts of each character. The function should ignore any non-alphabetic characters.
"""

def count_characters(s):
    """
    This function takes a string as input and returns a dictionary where the keys are unique 
    alphabetic characters in the string (ignoring case) and the values are the counts of each character.
    
    Parameters:
    s (str): The input string
    
    Returns:
    dict: A dictionary with unique alphabetic characters as keys and their counts as values
    """
    s = s.lower()
    char_count = {}
    for char in s:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count