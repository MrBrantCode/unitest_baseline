"""
QUESTION:
You have two arrays in this kata, every array contain only unique elements. Your task is to calculate number of elements in first array which also are in second array.
"""

def count_common_elements(array1, array2):
    """
    Counts the number of elements in array1 that are also present in array2.

    Parameters:
    array1 (list): The first array containing unique elements.
    array2 (list): The second array containing unique elements.

    Returns:
    int: The number of elements in array1 that are also in array2.
    """
    return sum(1 for x in array1 if x in array2)