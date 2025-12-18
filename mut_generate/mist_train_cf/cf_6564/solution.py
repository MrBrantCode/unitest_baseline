"""
QUESTION:
Write a function called `total_unique_elements` that calculates the total number of unique elements in a given 2D array. The array may contain sub-arrays with negative numbers, floating-point numbers, and prime numbers. The function should return the total count of unique elements in the array.
"""

def total_unique_elements(array):
    """
    Calculate the total number of unique elements in a given 2D array.

    Args:
        array (list): A 2D list containing sub-arrays with various elements.

    Returns:
        int: The total count of unique elements in the array.
    """
    # Flatten the 2D array into a single list
    flattened_array = [element for sub_array in array for element in sub_array]
    
    # Convert the list to a set to remove duplicates
    unique_elements = set(flattened_array)
    
    # Return the total count of unique elements
    return len(unique_elements)