"""
QUESTION:
Write a function named `remove_duplicates_sort` that takes a list of strings as input. The function should remove duplicates from the list, sort the remaining strings in descending order based on their length, and then sort strings with the same length in alphabetical order. The input list can contain up to 1 million strings and each string can have a length of up to 100 characters. The function should return the sorted list of unique strings.
"""

def remove_duplicates_sort(strings):
    """
    This function removes duplicates from the input list of strings, sorts the remaining strings in descending order based on their length, 
    and then sorts strings with the same length in alphabetical order.

    Args:
        strings (list): A list of strings

    Returns:
        list: A sorted list of unique strings
    """
    # Remove duplicates and empty strings
    unique_strings = set(strings)
    unique_strings.discard("")

    # Sort strings based on length in descending order and then by alphabetical order
    sorted_strings = sorted(unique_strings, key=lambda x: (-len(x), x))
    
    return sorted_strings