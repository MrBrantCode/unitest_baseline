"""
QUESTION:
Write a function called `convert_string_to_sorted_unique_integers` that takes a string of space-separated integers as input. The function should convert the string into a list of integers, remove any duplicate values, and sort the list in descending order. The function should return the resulting list of integers.
"""

def convert_string_to_sorted_unique_integers(s):
    """
    This function takes a string of space-separated integers, converts it into a list of integers, 
    removes any duplicate values, and sorts the list in descending order.

    Args:
        s (str): A string of space-separated integers.

    Returns:
        list: A list of integers in descending order with no duplicates.
    """
    return sorted(set(map(int, s.split())), reverse=True)