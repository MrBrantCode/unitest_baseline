"""
QUESTION:
Write a function named `sum_lengths` that takes an array of elements as input and returns the total length of the strings in the array that contain the letter 'a' and have a length greater than 3. The input array should have between 5 and 10 elements. Non-string elements should be excluded from the sum.
"""

def sum_lengths(arr):
    """
    Calculate the total length of strings in the array that contain the letter 'a' and have a length greater than 3.

    Args:
        arr (list): A list of elements.

    Returns:
        int: The total length of the strings that meet the conditions.
    """
    return sum(len(element) for element in arr if isinstance(element, str) and 'a' in element and len(element) > 3)