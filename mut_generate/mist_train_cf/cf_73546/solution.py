"""
QUESTION:
Create a function named `sort_tuple_frequency` that takes a tuple as input. The function should return a dictionary with elements of the tuple as keys and their frequencies as values. The dictionary should be sorted in descending order based on the values. The function should be case-insensitive, meaning it treats the same strings with different cases as the same key. The function should not have any restrictions on the type of elements in the tuple, so it should be able to handle both numeric and string elements.
"""

def sort_tuple_frequency(input_tuple):
    """
    This function takes a tuple as input and returns a dictionary with elements of the tuple as keys and their frequencies as values.
    The dictionary is sorted in descending order based on the values. The function is case-insensitive for string elements.

    Args:
        input_tuple (tuple): The input tuple containing elements of any type.

    Returns:
        dict: A dictionary with elements as keys and their frequencies as values, sorted in descending order.
    """
    # Create a dictionary with elements as keys and their frequencies as values
    freq_dict = {}
    for i in input_tuple:
        # Convert to lower case for case-insensitive string handling
        if isinstance(i, str):
            i = i.lower()
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1

    # Sort the dictionary items by value in descending order
    sorted_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))

    return sorted_dict