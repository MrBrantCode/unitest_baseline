"""
QUESTION:
Write a function named `unique_chars_in_string` that determines whether all the alphabetic characters within a provided string are unique and non-repetitive. The function should disregard non-alphabetic characters, treat uppercase and lowercase characters as the same, and return True if all alphabetic characters are unique and False otherwise. The function should also be efficient for extremely large input strings.
"""

def unique_chars_in_string(test_str):
    """
    This function returns True if all the alphabetic characters within the provided string are 
    unique and non-repetitive, otherwise it returns False.

    Parameters:
    test_str (str): The string to be checked.

    Returns:
    bool: Whether or not the string contains unique alphabetic characters.
    """

    # convert the string to lower case to treat 'P' and 'p' as the same character
    test_str = test_str.lower()

    # disregard non-alphabetic characters by ensuring that only alphabetic characters are
    # included in our character-checking process
    test_str = ''.join(c for c in test_str if c.isalpha())

    # check for the uniqueness of characters by comparing the length of the string with 
    # the number of unique characters (determined via the set function)
    return len(test_str) == len(set(test_str))