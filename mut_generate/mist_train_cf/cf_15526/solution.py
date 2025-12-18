"""
QUESTION:
Create a function `is_rotation` that checks if two given strings are a rotation of each other in either direction. The function takes two parameters: `string1` and `string2`, both consisting of lowercase alphabets and/or digits with lengths between 1 and 10^5. The function should return True if `string1` and `string2` are rotations of each other, and False otherwise.
"""

def is_rotation(string1, string2):
    """
    Checks if two given strings are a rotation of each other in either direction.
    
    Parameters:
    string1 (str): The first string to check.
    string2 (str): The second string to check.
    
    Returns:
    bool: True if string1 and string2 are rotations of each other, False otherwise.
    """
    # Check if the lengths of the strings are equal
    if len(string1) != len(string2):
        return False
    
    # Concatenate string1 with itself
    concatenated_string = string1 + string1
    
    # Check if string2 is a substring of the concatenated string
    return string2 in concatenated_string