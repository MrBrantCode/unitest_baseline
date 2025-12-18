"""
QUESTION:
Create a function named `convert_to_dict` that takes a list of elements as input, and returns a dictionary where each element in the list is used as a key and all values are of the same data type, specifically strings. The function should ensure that all keys in the dictionary are unique.
"""

def convert_to_dict(input_list):
    """
    This function converts a list of elements into a dictionary where each element in the list is used as a key and all values are of the same data type, specifically strings.
    
    Args:
    input_list (list): A list of elements to be converted into a dictionary.
    
    Returns:
    dict: A dictionary with unique keys and string values.
    """
    result_dict = {}
    for element in input_list:
        key = str(element)  # Convert the element to a string to use as the key
        value = str(element)  # Convert the element to a string to maintain the same data type for all values
        result_dict[key] = value
    return result_dict