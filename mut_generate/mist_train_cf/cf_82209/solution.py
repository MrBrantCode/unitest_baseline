"""
QUESTION:
Create a function `find_second_smallest` that takes a 3D array as input and returns the second smallest unique value in the array. If the array contains less than two distinct elements, the function should return `None`.
"""

def find_second_smallest(array_3d):
    # Flattening 3D array to 1D
    flat_list = [element for sublist1 in array_3d for sublist2 in sublist1 for element in sublist2]

    # Removing duplicates
    unique_list = list(set(flat_list))
    
    # Handling edge cases if flattened list contains less than 2 element
    if len(unique_list) < 2:
        return None

    # Using sorted function
    return sorted(unique_list)[1]