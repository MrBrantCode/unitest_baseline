"""
QUESTION:
Write a function named `find_vowels` that takes a string as input and returns a list of vowels found in the string, with all vowels converted to uppercase. The function should be case-insensitive when checking for vowels.
"""

def find_vowels(string):
    """
    This function takes a string as input and returns a list of vowels found in the string, 
    with all vowels converted to uppercase. The function is case-insensitive when checking for vowels.
    
    Parameters:
    string (str): The input string to find vowels in.
    
    Returns:
    list: A list of vowels found in the string, with all vowels converted to uppercase.
    """
    vowels = []
    for char in string:
        if char.lower() in "aeiou":
            vowels.append(char.upper())
    return vowels