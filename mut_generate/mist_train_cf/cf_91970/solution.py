"""
QUESTION:
Write a function `convert_to_uppercase` that takes a list as input, converts all string elements to uppercase, and returns the result in a new list. The function should not modify the original list, handle empty strings and non-string elements without errors, and return the result sorted in descending alphabetical order. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def convert_to_uppercase(input_list):
    """
    This function takes a list as input, converts all string elements to uppercase, 
    and returns the result in a new list. The function does not modify the original 
    list, handles empty strings and non-string elements without errors, and returns 
    the result sorted in descending alphabetical order.

    Args:
        input_list (list): A list containing string and/or non-string elements.

    Returns:
        list: A new list containing the uppercase string elements from the input list, 
              sorted in descending alphabetical order.
    """
    upper_list = [string.upper() for string in input_list if isinstance(string, str)]
    return sorted(upper_list, reverse=True)