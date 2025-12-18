"""
QUESTION:
Implement a function named `sum_prefix` that takes an array of integers as input and returns the prefix sum of unique negative integers. If the array contains a non-negative number, return None. If the array is empty or contains non-integer elements, return None. The function should handle repeated erroneous elements and calculate the sum starting with the smallest absolute value.
"""

def sum_prefix(arr):
    """
    This function takes an array of integers as input and returns the prefix sum of unique negative integers.
    If the array contains a non-negative number, return None. If the array is empty or contains non-integer elements, return None.

    Args:
        arr (list): A list of integers.

    Returns:
        int or None: The sum of unique negative integers or None based on the conditions.
    """

    if arr == [] or arr is None: 
        return None
    
    unique_negatives = set()

    for i in arr:
        if not isinstance(i, int): 
            continue
        if i >= 0: 
            return None
        else:
            unique_negatives.add(i)
            
    return sum(unique_negatives)