"""
QUESTION:
Design a function `convertAndSort` that takes a list of characters as input, filters out non-alphabet characters, converts the remaining characters to uppercase, sorts them in ascending order, and returns the result as a string. The input list may contain both uppercase and lowercase letters. The function should have a time complexity of O(n log n), where n is the length of the input list.
"""

def convertAndSort(lst):
    """
    This function takes a list of characters as input, filters out non-alphabet characters, 
    converts the remaining characters to uppercase, sorts them in ascending order, 
    and returns the result as a string.

    Parameters:
    lst (list): A list of characters.

    Returns:
    str: A string containing the filtered, converted, and sorted characters.
    """
    # Filter out non-alphabet characters and convert to uppercase
    letters = [char.upper() for char in lst if char.isalpha()]
    
    # Sort the letters in ascending order
    sorted_letters = sorted(letters)
    
    # Join the sorted letters into a string and return the result
    return ''.join(sorted_letters)