"""
QUESTION:
Create a function `filter_names` that takes a list of names as input and returns a new list containing names that meet two conditions: the length of the name is greater than 4 and the name contains at least one vowel (ignoring case sensitivity).
"""

def filter_names(names):
    """
    This function filters a list of names and returns a new list containing names 
    that have a length greater than 4 and contain at least one vowel (ignoring case sensitivity).
    
    Parameters:
    names (list): A list of names
    
    Returns:
    list: A list of filtered names
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [name for name in names if len(name) > 4 and any(vowel in name.lower() for vowel in vowels)]