"""
QUESTION:
Create a function named `sort_lists` that takes two parameters: a list of integers and a list of strings. The function should sort the list of integers in descending order and the list of strings in ascending order based on the sum of the ASCII values of the characters in each string. The function should return the two sorted lists.
"""

def sort_lists(num_list, string_list):
    """
    Sorts a list of integers in descending order and a list of strings in ascending order based on the sum of ASCII values.

    Args:
        num_list (list): A list of integers.
        string_list (list): A list of strings.

    Returns:
        tuple: A tuple containing the sorted list of integers and the sorted list of strings.
    """
    sorted_num_list = sorted(num_list, reverse=True)
    sorted_string_list = sorted(string_list, key=lambda s: sum(ord(c) for c in s))
    return sorted_num_list, sorted_string_list