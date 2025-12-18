"""
QUESTION:
Create a function named `array_operations` that takes two lists of integers `arr1` and `arr2` as input and returns two lists. The first list should contain the sums of corresponding elements of `arr1` and `arr2`, and the second list should contain the differences of corresponding elements of `arr1` and `arr2`. The function should assume that both input lists have the same length.
"""

def array_operations(arr1, arr2):
    """
    Calculate the sums and differences of corresponding elements in two lists.
    
    Args:
        arr1 (list): The first list of integers.
        arr2 (list): The second list of integers.
    
    Returns:
        tuple: A tuple containing two lists. The first list contains the sums of corresponding elements,
            and the second list contains the differences of corresponding elements.
    """
    sums = [a + b for a, b in zip(arr1, arr2)]
    differences = [a - b for a, b in zip(arr1, arr2)]
    return sums, differences