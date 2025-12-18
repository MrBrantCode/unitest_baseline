"""
QUESTION:
Write a function named `sum_dict_values` that takes a list of tuples as input, where each tuple contains a key-value pair. The function should create a dictionary where each key is associated with a list of its corresponding values. If a key already exists in the dictionary, the value should be appended to the existing list. After constructing the dictionary, the function should calculate the sum of each list of values and store the sum as the new value for each key, replacing the original list.
"""

def sum_dict_values(tuple_list):
    """
    This function takes a list of tuples as input, creates a dictionary where each key is associated with a list of its corresponding values,
    and then calculates the sum of each list of values.

    Args:
        tuple_list (list): A list of tuples, where each tuple contains a key-value pair.

    Returns:
        dict: A dictionary where each key is associated with the sum of its corresponding values.
    """

    # Initialize an empty dictionary to store the key-value pairs
    dict1 = {}

    # Iterate over each tuple in the input list
    for item in tuple_list:
        key = item[0]
        value = item[1]

        # If the key already exists in the dictionary, append the value to the existing list
        if key in dict1:
            dict1[key].append(value)
        # If the key does not exist, create a new key-value pair with the value as a list
        else:
            dict1[key] = [value]

    # Iterate over each key-value pair in the dictionary and calculate the sum of the list of values
    for key, value in dict1.items():
        dict1[key] = sum(value)

    # Return the updated dictionary
    return dict1