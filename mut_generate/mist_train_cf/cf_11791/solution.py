"""
QUESTION:
Implement a function named `remove_elements` that takes two parameters, `first_array` and `second_array`, both of which are array-like structures containing elements of any type, including nested arrays. The function should return a new array containing all elements from `first_array` that do not appear in `second_array`. If an element in `first_array` is a nested array, the function should recursively remove any elements from it that appear in `second_array`.
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