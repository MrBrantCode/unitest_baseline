"""
QUESTION:
Write a function named `mergeAndSort` that takes in multiple arrays of varying data types and merges them into a single sorted array in ascending order. The function should handle and sort integers, floating numbers, and strings simultaneously. It should also efficiently handle large data inputs up to 10,000 elements. The input will be a list of arrays, where each array can contain integers, floats, and strings.
"""

def mergeAndSort(input):
    """
    This function merges multiple arrays of varying data types into a single sorted array in ascending order.
    
    Args:
        input (list): A list of arrays containing integers, floats, and strings.
    
    Returns:
        list: A single sorted array.
    """
    merged = [item for sublist in input for item in sublist]
    return sorted(merged, key=lambda x: (not isinstance(x, (int, float)), str(x)))