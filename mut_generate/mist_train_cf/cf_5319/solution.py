"""
QUESTION:
Write a function `clean_list` that takes a list of strings as input. The function should convert all strings to lowercase, remove any strings containing non-alphabetical characters, eliminate duplicates, and sort the resulting list in alphabetical order.
"""

def clean_list(input_list):
    """
    This function takes a list of strings, converts them to lowercase, removes non-alphabetical strings, 
    eliminates duplicates, and sorts the list in alphabetical order.

    Args:
        input_list (list): A list of strings.

    Returns:
        list: A cleaned and sorted list of strings.
    """
    return sorted(set([word.lower() for word in input_list if word.isalpha()]))