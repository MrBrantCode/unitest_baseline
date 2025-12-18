"""
QUESTION:
Write a function named `flatten_array` that calculates the total number of unique positive integers in a given array of sub-arrays, where each sub-array can contain positive integers, negative integers, or floating-point numbers.
"""

def entance(arr):
    """Calculates the total number of unique positive integers in a given array of sub-arrays."""
    
    def flatten_array(sub_arr):
        """Flattens a multi-dimensional array into a one-dimensional array."""
        flattened = []
        for element in sub_arr:
            if isinstance(element, list):
                flattened.extend(flatten_array(element))
            else:
                flattened.append(element)
        return flattened
    
    flattened_arr = flatten_array(arr)
    unique_positive_elements = set([element for element in flattened_arr if isinstance(element, int) and element > 0])
    return len(unique_positive_elements)