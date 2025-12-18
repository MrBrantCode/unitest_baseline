"""
QUESTION:
Write a function named `filter_strings` that takes a list of strings and a length as input, and returns a new list containing only the strings that have a length greater than the given number and do not contain any special characters. The function should ignore strings that have lengths less than or equal to the given number and strings that contain special characters.
"""

def filter_strings(lst, length):
    """
    Filters a list of strings based on length and special characters.

    Args:
    lst (list): A list of strings.
    length (int): The minimum length of strings to be included.

    Returns:
    list: A new list containing strings with lengths greater than the given number and no special characters.
    """
    return [string for string in lst if len(string) > length and string.isalnum()]