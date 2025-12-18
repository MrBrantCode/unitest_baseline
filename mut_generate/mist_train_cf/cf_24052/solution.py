"""
QUESTION:
Create a function named `char_count` that takes a string as input and returns a dictionary where each key is a unique character from the string and the corresponding value is the number of occurrences of that character in the string.
"""

def char_count(s):
    """
    This function takes a string as input and returns a dictionary where each key is a unique character 
    from the string and the corresponding value is the number of occurrences of that character in the string.

    Parameters:
    s (str): The input string.

    Returns:
    dict: A dictionary containing the frequency of each unique character in the string.
    """
    return {char: s.count(char) for char in set(s)}