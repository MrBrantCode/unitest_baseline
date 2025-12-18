"""
QUESTION:
Create a function `filter_dict` that takes a dictionary as input and returns a new dictionary containing only the key-value pairs from the original dictionary where the values are greater than or equal to 10.
"""

def filter_dict(input_dict):
    """
    Returns a new dictionary containing only the key-value pairs 
    from the original dictionary where the values are greater than or equal to 10.

    Args:
        input_dict (dict): The input dictionary to filter.

    Returns:
        dict: A new dictionary with filtered key-value pairs.
    """
    return {key: value for key, value in input_dict.items() if value >= 10}