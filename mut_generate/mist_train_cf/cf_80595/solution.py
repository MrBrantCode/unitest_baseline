"""
QUESTION:
Create a function named `capitalize_fruit_names` that takes a list of strings representing fruit names as input. The function should capitalize every fruit name in the list and replace the original fruit names with their capitalized versions. The function should return the modified list. The input list may contain any number of fruit names.
"""

def capitalize_fruit_names(fruit_list):
    """
    Capitalize every fruit name in the list and replace the original fruit names with their capitalized versions.

    Args:
        fruit_list (list): A list of strings representing fruit names.

    Returns:
        list: The modified list with all fruit names capitalized.
    """
    for i, fruit in enumerate(fruit_list):
        fruit_list[i] = fruit.capitalize()
    return fruit_list