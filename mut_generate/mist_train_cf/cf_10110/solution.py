"""
QUESTION:
Convert a list of strings to a sorted list of integers, skipping any non-integer strings, and return the sum of the integers in the list. 

Write a function named `convert_and_sum` that takes a list of strings as input. The function should convert the strings that represent integers to integers and store them in a list, ignoring any strings that do not represent integers. The list of integers should be sorted in ascending order, and the function should return the sum of the integers in the list.
"""

def convert_and_sum(strings):
    """
    Convert a list of strings to a sorted list of integers, skipping any non-integer strings, 
    and return the sum of the integers in the list.

    Args:
        strings (list): A list of strings.

    Returns:
        int: The sum of the integers in the sorted list.
    """
    integers = [int(string) for string in strings if string.isdigit()]
    integers.sort()
    return sum(integers)