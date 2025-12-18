"""
QUESTION:
Create a function `capitalize_first_letter` that takes a list of strings as input. The function should capitalize the first letter of each string. However, if a string starts with a number or special character, capitalize the second letter instead. The function should return the modified list of strings. Assume the input list contains strings of at least two characters.
"""

def capitalize_first_letter(strings):
    """
    Capitalize the first letter of each string in the input list.
    If a string starts with a number or special character, capitalize the second letter instead.

    Args:
        strings (list): A list of strings.

    Returns:
        list: The modified list of strings.
    """
    modified_list = []
    for string in strings:
        if string[0].isalpha():
            modified_list.append(string[0].upper() + string[1:])
        else:
            modified_list.append(string[0] + string[1].upper() + string[2:])
    return modified_list