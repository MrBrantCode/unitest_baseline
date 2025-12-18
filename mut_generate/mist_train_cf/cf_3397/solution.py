"""
QUESTION:
Create a function `capitalize_list` that takes a list of strings as input. Iterate over each string in the list, capitalizing the first letter if it is alphanumeric, otherwise capitalizing the second letter. Remove any duplicates from the modified list and return the result in reverse order.
"""

def capitalize_list(lst):
    """
    Capitalize the first alphanumeric character in each string of the list.
    If the first character is not alphanumeric, capitalize the second character.
    Remove duplicates and return the result in reverse order.
    
    Args:
        lst (list): A list of strings.
    
    Returns:
        list: The modified list of strings.
    """
    modified_list = []
    for string in lst:
        if len(string) > 1:
            if string[0].isalnum():
                modified_list.append(string[0].capitalize() + string[1:])
            else:
                modified_list.append(string[0] + string[1].capitalize() + string[2:])
        elif len(string) == 1:
            modified_list.append(string.capitalize())
        else:
            modified_list.append(string)
    modified_list = list(dict.fromkeys(modified_list))
    modified_list.reverse()
    return modified_list