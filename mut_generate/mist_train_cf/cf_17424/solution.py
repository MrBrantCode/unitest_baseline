"""
QUESTION:
Write a function `add(arr)` that calculates the sum of all numbers in the given array. The array can contain nested arrays or objects. If it does, the function should recursively traverse the nested arrays and objects to include all numbers in the sum.
"""

def add(arr):
    """
    This function calculates the sum of all numbers in the given array.
    It recursively traverses nested arrays and objects to include all numbers in the sum.

    Args:
        arr: The input array that can contain nested arrays or objects.

    Returns:
        The sum of all numbers in the array.
    """
    total = 0
    for element in arr:
        if isinstance(element, list):
            total += add(element)
        elif isinstance(element, dict):
            total += add(list(element.values()))
        elif isinstance(element, (int, float)):
            total += element
    return total