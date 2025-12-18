"""
QUESTION:
Create a function `create_sorted_dict` that takes a dictionary as input. The function should return a dictionary where each value is the square of the original value and a list of tuples containing the key-value pairs from the dictionary, sorted in descending order based on the squared values.
"""

def create_sorted_dict(input_dict):
    """
    This function takes a dictionary as input, squares its values, and returns 
    a dictionary with the squared values and a list of tuples containing the 
    key-value pairs from the dictionary, sorted in descending order based on 
    the squared values.

    Args:
        input_dict (dict): The input dictionary.

    Returns:
        tuple: A dictionary with squared values and a list of sorted tuples.
    """
    squared_dict = {key: value ** 2 for key, value in input_dict.items()}
    sorted_tuples = sorted(squared_dict.items(), key=lambda x: x[1], reverse=True)

    return squared_dict, sorted_tuples