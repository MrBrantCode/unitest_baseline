"""
QUESTION:
Write a function `find_target_string(list_strings, target_string)` that takes a list of strings and a target string as input. The function should return the index of the target string in the list if it exists. If the target string is not found, return the index of the first occurrence of a string that starts with the same letter as the target string. If no such string is found, return -1.
"""

def find_target_string(list_strings, target_string):
    """
    This function finds the index of a target string in a list of strings.
    If the target string is not found, it returns the index of the first occurrence 
    of a string that starts with the same letter as the target string. If no such 
    string is found, it returns -1.

    Parameters:
    list_strings (list): A list of strings.
    target_string (str): The target string to be found.

    Returns:
    int: The index of the target string or the index of a string that starts with 
    the same letter as the target string, or -1 if no such string is found.
    """
    for i in range(len(list_strings)):
        if list_strings[i] == target_string:
            return i
        elif list_strings[i][0] == target_string[0]:
            return i
    return -1