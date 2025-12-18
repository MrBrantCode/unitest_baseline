"""
QUESTION:
Write a function `find_substring_index` that takes two parameters: a string `main_string` and a substring `sub_string`. The function should return the index of the first occurrence of the `sub_string` in the `main_string`, with the search being case-insensitive and matching the entire word only.
"""

def find_substring_index(main_string, sub_string):
    """
    Returns the index of the first occurrence of the sub_string in the main_string.
    The search is case-insensitive and matches the entire word only.

    Parameters:
    main_string (str): The string to search in.
    sub_string (str): The substring to search for.

    Returns:
    int: The index of the first occurrence of the sub_string, or -1 if not found.
    """
    return main_string.lower().find(sub_string.lower())