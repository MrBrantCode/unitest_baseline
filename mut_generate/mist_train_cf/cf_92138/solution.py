"""
QUESTION:
Create a function called `get_vowels` that takes a string as input and returns a list of vowels from the string. The function should be case-insensitive and only include the characters 'a', 'e', 'i', 'o', and 'u' as vowels.
"""

def get_vowels(string):
    """
    Returns a list of vowels from the input string.
    
    The function is case-insensitive and only includes 'a', 'e', 'i', 'o', and 'u' as vowels.
    
    Parameters:
    string (str): The input string.
    
    Returns:
    list: A list of vowels in the string.
    """
    vowels = [char for char in string if char.lower() in ['a', 'e', 'i', 'o', 'u']]
    return vowels