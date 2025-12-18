"""
QUESTION:
Write a function `remove_and_sort` that takes a string as input, removes all non-alphabet characters, and returns the resulting string with its alphabets sorted in descending order based on their ASCII values.
"""

def remove_and_sort(string):
    """
    Removes non-alphabet characters from the input string and returns the resulting string 
    with its alphabets sorted in descending order based on their ASCII values.
    
    Parameters:
    string (str): The input string.
    
    Returns:
    str: The string with non-alphabet characters removed and alphabets sorted in descending order.
    """
    new_string = "".join(char for char in string if char.isalpha())
    return "".join(sorted(new_string, reverse=True))