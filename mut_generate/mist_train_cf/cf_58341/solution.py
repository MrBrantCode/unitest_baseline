"""
QUESTION:
Create a function `sort_array()` that takes an array of alphanumeric strings as input, and returns the array sorted in ascending order based on the numerical part of each string. The function should extract the numerical part of each string, convert it to an integer, and use it as the comparison key for sorting. The array contains only alphanumeric strings where the numerical part is contiguous and does not contain leading zeros.
"""

def sort_array(samples):
    """
    Sorts an array of alphanumeric strings based on the numerical part of each string.

    Args:
    samples (list): A list of alphanumeric strings.

    Returns:
    list: The sorted list of alphanumeric strings.
    """
    return sorted(samples, key=lambda x: int(''.join(filter(str.isdigit, x))))