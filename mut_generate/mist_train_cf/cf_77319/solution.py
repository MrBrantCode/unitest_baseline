"""
QUESTION:
Create a function called `search_element` that takes a list of strings and a target string as input, sorts the list alphabetically without using built-in sorting functions, and returns the position of the target string in the sorted list. The position should be zero-indexed, and if the target string is not found, return -1.
"""

def search_element(item_list, element):
    """
    Sorts a list of strings alphabetically without using built-in sorting functions 
    and returns the position of a target string in the sorted list.

    Args:
    item_list (list): A list of strings.
    element (str): The target string to be searched.

    Returns:
    int: The position of the target string in the sorted list (zero-indexed). 
         Returns -1 if the target string is not found.
    """
    for i in range(len(item_list)):
        for j in range(len(item_list) - 1):
            if item_list[j] > item_list[j + 1]:
                item_list[j], item_list[j + 1] = item_list[j + 1], item_list[j]
    for i in range(len(item_list)):
        if item_list[i] == element:
            return i
    return -1