"""
QUESTION:
Create a function called `reverse_strings` that takes a list of strings as input, reverses each string, and returns the reversed list, excluding any strings that contain non-alphabetic characters.
"""

def reverse_strings(list_of_strings):
    """
    This function takes a list of strings as input, reverses each string, 
    and returns the reversed list, excluding any strings that contain non-alphabetic characters.

    Args:
        list_of_strings (list): A list of strings.

    Returns:
        list: The reversed list of strings with non-alphabetic strings excluded.
    """
    return [word[::-1] for word in list_of_strings if word.isalpha()]