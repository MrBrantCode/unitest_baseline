"""
QUESTION:
Write a function `find_substrings(string_list, sub_string)` that accepts a list of strings `string_list` and a unique string `sub_string` as arguments. The function should return a list of all strings in `string_list` that contain `sub_string`, ignoring case sensitivity. If no matches are found, it should return 'No matches found'. If `string_list` or `sub_string` is empty, it should return 'Invalid input'.
"""

def find_substrings(string_list, sub_string):
    """
    Returns a list of all strings in string_list that contain sub_string, ignoring case sensitivity.
    
    Args:
    string_list (list): A list of strings.
    sub_string (str): A unique string to search for in string_list.
    
    Returns:
    list: A list of strings that contain sub_string. If no matches are found, returns 'No matches found'. If string_list or sub_string is empty, returns 'Invalid input'.
    """
    # Check for empty string_list or sub_string
    if not string_list or not sub_string:
        return 'Invalid input'
    
    # Convert sub_string to lower case
    sub_string = sub_string.lower()
    
    # Will hold the list of strings that contain the sub_string
    matches = [i for i in string_list if sub_string in i.lower()]
    
    # if sub_string is not in any of strings in string_list
    return matches if matches else 'No matches found'