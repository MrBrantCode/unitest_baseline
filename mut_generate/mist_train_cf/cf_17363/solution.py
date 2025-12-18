"""
QUESTION:
Write a function called `findMinimum` that finds the minimum element in a nested array of values. The function should take two parameters: `nested_array` and `comparison_function`. The `nested_array` can have an arbitrary number of levels and dimensions, and each level can have an arbitrary number of elements. The `comparison_function` should take two elements and return -1, 0, or 1 based on the comparison criteria. The function should return the minimum element in the nested array. The function should be able to handle non-integer elements and have a time complexity of O(n), where n is the total number of elements in the nested array.
"""

def findMinimum(nested_array, comparison_function):
    """
    This function finds the minimum element in a nested array of values.
    
    Args:
    nested_array (list): The input array which can be nested and have arbitrary dimensions.
    comparison_function (function): A function that compares two elements and returns -1, 0, or 1.
    
    Returns:
    The minimum element in the nested array.
    """
    
    # Initialize minElement as infinity
    minElement = float('inf')
    
    # Define a helper function to recursively traverse the nested array
    def traverse(array):
        nonlocal minElement  # Use nonlocal keyword to modify minElement inside the nested function
        
        for element in array:
            if isinstance(element, list):
                traverse(element)  # Recursively call traverse on nested arrays
            else:
                # Compare the element with minElement using the comparison function
                if comparison_function(element, minElement) < 0:
                    minElement = element
    
    # Start traversing the nested array from the root
    traverse(nested_array)
    
    return minElement