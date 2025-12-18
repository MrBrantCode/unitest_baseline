"""
QUESTION:
Write a function named `extract_element` that takes a tuple of strings and a target string as input, and returns the target string if found in one of the strings in the tuple. If the target string is not found, the function should return "Element not found". The function should also be able to extract a substring from the found string. For example, if the tuple contains the string "Pineapple" and the target string is "apple", the function should return "apple".
"""

def extract_element(tuple_of_strings, target_string):
    """
    This function takes a tuple of strings and a target string as input, 
    and returns the target string if found in one of the strings in the tuple. 
    If the target string is not found, the function returns "Element not found".
    
    Args:
    tuple_of_strings (tuple): A tuple of strings.
    target_string (str): The target string to be found.
    
    Returns:
    str: The target string if found, "Element not found" otherwise.
    """
    for string in tuple_of_strings:
        if target_string in string:
            return target_string
    return "Element not found"