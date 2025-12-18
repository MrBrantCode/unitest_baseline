"""
QUESTION:
Implement a function called "sort_list" that takes two lists as arguments: a list of numbers and a list of strings. The function should return a combined list where the numbers are sorted in descending order and the strings are sorted in ascending order based on the sum of their ASCII values.
"""

def sort_list(num_list, string_list):
    """
    Combines two lists, one containing numbers and the other strings, 
    sorting the numbers in descending order and the strings in ascending 
    order based on the sum of their ASCII values.

    Args:
        num_list (list): A list of numbers.
        string_list (list): A list of strings.

    Returns:
        list: A combined list of sorted numbers and strings.
    """
    num_list.sort(reverse=True)
    string_list.sort(key=lambda s: sum(ord(c) for c in s))
    return num_list + string_list