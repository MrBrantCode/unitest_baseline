"""
QUESTION:
Implement a function `remove_elements(first_array, second_array)` that takes two array-like structures as input and returns a new array containing all elements from `first_array` that do not appear in `second_array`. The function should handle cases where `second_array` is a nested array and remove elements recursively. The function should work with arrays containing any type of element, including nested arrays.
"""

def remove_elements(first_array, second_array):
    # Create a new list to store the result
    result = []
    
    # Iterate over the elements in the first array
    for element in first_array:
        # If the element is not in the second array, add it to the result
        if element not in second_array:
            # If the element is a list, recursively remove elements from it
            if isinstance(element, list):
                element = remove_elements(element, second_array)
            
            result.append(element)
    
    return result