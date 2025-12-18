"""
QUESTION:
Write a function called `process_strings` that takes a list of strings as input. The function should print each individual string in uppercase, reverse the order of the strings in the list, and then concatenate all the reversed strings into a single string separated by a comma, returning the concatenated string in uppercase.
"""

def process_strings(string_list):
    """
    This function processes a list of strings. It prints each string in uppercase, 
    reverses the order of the strings, and returns the reversed strings concatenated 
    into a single string separated by a comma in uppercase.

    Args:
        string_list (list): A list of strings.

    Returns:
        str: The concatenated string in uppercase.
    """
    # Print each individual string in uppercase
    for string in string_list:
        print(string.upper())

    # Reverse the order of the strings
    string_list.reverse()

    # Concatenate all the reversed strings into a single string, separated by a comma
    reversed_string = ", ".join(string_list)

    return reversed_string.upper()