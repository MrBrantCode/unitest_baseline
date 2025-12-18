"""
QUESTION:
Write a function named `find_max_value_and_index` that takes a list of integers as input and returns the maximum number in the list along with its positional index. If the list is empty, return a message indicating that the list is empty. The function should have a time complexity of O(n) to handle large datasets efficiently.
"""

def find_max_value_and_index(lst):
    """
    This function finds the maximum number in a list and its positional index.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    tuple: A tuple containing the maximum number and its index. If the list is empty, it returns a message indicating that the list is empty.
    """
    if lst:
        max_value = max_index = None

        # Go through each element only once
        for index, value in enumerate(lst):
            # Update max_value and max_index as we find bigger values
            if max_value is None or value > max_value:
                max_value = value
                max_index = index
                
        return max_value, max_index
    else:
        return "The list is empty"