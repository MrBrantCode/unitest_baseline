"""
QUESTION:
Create a function named `check_and_multiply` that takes a dictionary and a key as input. The dictionary should contain a maximum of 100 key-value pairs, where keys are alphanumeric strings with a length between 1 and 10 characters and values are positive integers. The function should return the corresponding value multiplied by 2 if the key is present in the dictionary, otherwise return -1.
"""

def check_and_multiply(input_dict, key):
    """
    This function checks if a given key is present in the dictionary.
    If the key is present, it returns the corresponding value multiplied by 2.
    If the key is not present, it returns -1.

    Args:
        input_dict (dict): A dictionary containing alphanumeric keys with a length between 1 and 10 characters and positive integer values.
        key (str): The key to be checked in the dictionary.

    Returns:
        int: The value corresponding to the key multiplied by 2 if the key is present, otherwise -1.
    """

    if key in input_dict:
        return input_dict[key] * 2
    else:
        return -1