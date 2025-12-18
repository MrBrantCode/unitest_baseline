"""
QUESTION:
Create a function `find_unique` that takes a list of arrays as input. For each array, the function should check if it contains all unique values. If an array contains all unique values, it should be considered for the output. The function should return all arrays with the maximum number of unique values.
"""

def find_unique(arr_list):
    """
    This function takes a list of arrays as input. It checks each array for unique values, 
    then returns all arrays with the maximum number of unique values.

    Args:
    arr_list (list): A list of arrays.

    Returns:
    list: A list of arrays with the maximum number of unique values.
    """
    unique_list = []
    max_unique_len = 0
    for arr in arr_list:
        if len(arr) == len(set(arr)):  # if arr contains all unique values
            unique_list.append(arr)
            max_unique_len = max(max_unique_len, len(arr))  # update max unique length
    # returning all arrays which have max unique length
    return [arr for arr in unique_list if len(arr) == max_unique_len]