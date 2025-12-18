"""
QUESTION:
Create a function `find_unique_char` that takes two parameters: a string and a correction map. The function should return a tuple containing the first non-repeating character in the string after corrections have been made using the correction map, and its corresponding index location. The correction map should be applied to all characters in the string, not just the unique one. If no unique character exists after corrections, the function should return `None`.
"""

def find_unique_char(string, correction_map):
    """
    This function finds the first non-repeating character in a string after corrections have been made using a correction map.

    Parameters:
    string (str): The input string.
    correction_map (dict): A dictionary containing corrections to be made in the string.

    Returns:
    tuple: A tuple containing the first non-repeating character and its index location. If no unique character exists, returns None.
    """

    # Create a corrected string based on the provided correction map
    corrected_string = ""
    for char in string:
        if char in correction_map:
            corrected_string += correction_map[char]
        else:
            corrected_string += char
    
    # Find the first non-repeating character in the corrected string
    for index, char in enumerate(corrected_string):
        if corrected_string.count(char) == 1:
            return (char, index)
    
    # If no unique character exists, return None
    return None