"""
QUESTION:
Implement a function named `filter_array` that takes an array of mixed data types as input. The function should remove all integers from the array, preserve the order of the remaining elements, and exclude any strings that start with a capital letter. The resulting array should only contain strings that start with a lowercase letter and floating-point numbers. If there are no strings or floating-point numbers left after the removal, return an empty array.
"""

def filter_array(arr):
    """
    Removes integers from the array, preserves the order of the remaining elements,
    and excludes any strings that start with a capital letter.

    Args:
    arr (list): A list of mixed data types.

    Returns:
    list: A filtered list containing only strings that start with a lowercase letter and floating-point numbers.
    """
    filtered_arr = []
    for element in arr:
        if type(element) == str:
            if element[0].islower():
                filtered_arr.append(element)
        elif type(element) == float:
            filtered_arr.append(element)
    return filtered_arr