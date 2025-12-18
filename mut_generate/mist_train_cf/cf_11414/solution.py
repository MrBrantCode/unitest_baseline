"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of strings as input. The function should return a list of unique strings (case-insensitive), sorted in descending order of their lengths, along with the count of unique strings and the sum of their lengths. The function should treat 'a' and 'A' as the same string.
"""

def remove_duplicates(string_list):
    """
    This function removes duplicates from a list of strings (case-insensitive), 
    sorts them in descending order of their lengths, and returns the list along 
    with the count of unique strings and the sum of their lengths.

    Args:
        string_list (list): A list of strings.

    Returns:
        tuple: A tuple containing a list of unique strings, their count, and the sum of their lengths.
    """
    unique_strings = list(set(string.lower() for string in string_list))
    unique_strings.sort(key=len, reverse=True)
    count = len(unique_strings)
    length_sum = sum(len(string) for string in unique_strings)
    return unique_strings, count, length_sum