"""
QUESTION:
Write a function `process_arrays` that takes a list of numerical arrays as input, where each array may contain duplicate values and may not be sorted. The function should return a new list of arrays, where each array contains all elements from the original arrays, sorted in descending order within each array, and the arrays are sorted in descending order based on their maximum elements. If there are multiple arrays with the same maximum element, their order in the output list should be the same as in the input list. 

Note that the function should handle lists of arrays of varying lengths and may contain duplicate values.
"""

def process_arrays(arrays):
    """
    Process a list of numerical arrays by sorting each array in descending order
    and then sorting the arrays based on their maximum elements in descending order.

    Args:
        arrays (list): A list of numerical arrays.

    Returns:
        list: A new list of arrays, where each array contains all elements from the
              original arrays, sorted in descending order within each array, and the
              arrays are sorted in descending order based on their maximum elements.
    """
    return sorted([sorted(array, reverse=True) for array in arrays], 
                  key=max, reverse=True)