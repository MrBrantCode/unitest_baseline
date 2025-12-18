"""
QUESTION:
Create a function named `findStrings` that takes an array of strings as input and returns a new array containing only the strings that start with the letter "a" and end with the letter "e". The function should consider only lowercase strings for this criteria, but return the original case strings. If there are no strings meeting this criteria, return an empty array.
"""

def findStrings(arr):
    """
    This function takes an array of strings as input and returns a new array containing 
    only the strings that start with the letter "a" and end with the letter "e". The 
    function considers only lowercase strings for this criteria, but returns the 
    original case strings. If there are no strings meeting this criteria, return an 
    empty array.

    Parameters:
    arr (list): A list of strings

    Returns:
    list: A list of strings that start with 'a' and end with 'e'
    """
    return [s for s in arr if s.lower().startswith('a') and s.lower().endswith('e')]