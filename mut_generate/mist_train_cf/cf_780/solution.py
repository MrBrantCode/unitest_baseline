"""
QUESTION:
Create a function `convert_to_sorted_string` that takes a list of integers as input and returns a string. The function should sort the integers in ascending order, remove duplicates, and enclose the result in square brackets. The output should be a comma-separated string. The time complexity of the solution should be less than O(nlogn).
"""

def convert_to_sorted_string(lst):
    """
    Converts a list of integers into a comma-separated string in ascending order without duplicates, 
    enclosed in square brackets.

    Args:
        lst (list): A list of integers.

    Returns:
        str: A comma-separated string in ascending order without duplicates, enclosed in square brackets.
    """
    return '[' + ', '.join(map(str, sorted(set(lst)))) + ']'