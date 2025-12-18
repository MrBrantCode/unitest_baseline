"""
QUESTION:
Write a function named `swap_and_sort_dict` that takes a dictionary as input and returns a new dictionary. The function should swap the keys and values of the input dictionary, filter out the key-value pairs where the original value (now key) is less than or equal to 15, and sort the remaining key-value pairs in descending order based on the original value (now key). The function should not use any built-in functions or methods that directly swap the values of dictionaries.
"""

def swap_and_sort_dict(input_dict):
    """
    This function swaps the keys and values of the input dictionary, 
    filters out the key-value pairs where the original value (now key) is less than or equal to 15, 
    and sorts the remaining key-value pairs in descending order based on the original value (now key).

    Args:
        input_dict (dict): The input dictionary to be processed.

    Returns:
        dict: A new dictionary with the key-value pairs swapped, filtered, and sorted.
    """

    # Swapping the values of the dictionary
    swapped_dic = {value: key for key, value in input_dict.items()}

    # Creating a new dictionary with values greater than 15
    new_dic = {key: value for key, value in swapped_dic.items() if key > 15}

    # Sorting the new dictionary in descending order
    sorted_dic = dict(sorted(new_dic.items(), key=lambda item: item[0], reverse=True))

    return sorted_dic