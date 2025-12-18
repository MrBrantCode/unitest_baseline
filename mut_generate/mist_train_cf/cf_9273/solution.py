"""
QUESTION:
Write a function called `common_elements` that takes five lists as input and returns a dictionary where the keys are the elements that are present in all the lists and the values represent the number of lists each common element appears in.
"""

def common_elements(arr1, arr2, arr3, arr4, arr5):
    """
    This function takes five lists as input and returns a dictionary where the keys are the elements 
    that are present in all the lists and the values represent the number of lists each common element appears in.

    Args:
        arr1 (list): The first list.
        arr2 (list): The second list.
        arr3 (list): The third list.
        arr4 (list): The fourth list.
        arr5 (list): The fifth list.

    Returns:
        dict: A dictionary where the keys are the common elements and the values represent the number of lists each common element appears in.
    """

    # Create a set for each array
    sets = [set(arr1), set(arr2), set(arr3), set(arr4), set(arr5)]

    # Find the intersection of all sets
    common_elements = set.intersection(*sets)

    # Create a dictionary to keep track of the number of arrays each common element appears in
    common_count = {element: 0 for element in common_elements}

    # Count the number of arrays each common element appears in
    for array in sets:
        for element in common_elements:
            if element in array:
                common_count[element] += 1

    return common_count