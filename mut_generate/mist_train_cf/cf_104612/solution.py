"""
QUESTION:
Create a function called `remove_duplicates_and_lower_case` that takes a list of strings as input. The function should return a list of strings where all strings are in lowercase and duplicates have been removed.
"""

def remove_duplicates_and_lower_case(input_list):
    """
    This function takes a list of strings, converts them to lowercase, and removes duplicates.
    
    Args:
    input_list (list): A list of strings.
    
    Returns:
    list: A list of strings where all strings are in lowercase and duplicates have been removed.
    """
    return list(set([word.lower() for word in input_list]))