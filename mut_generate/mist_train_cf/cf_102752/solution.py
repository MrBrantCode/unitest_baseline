"""
QUESTION:
Create a function named `multiply_values` that takes a dictionary as input and returns a new dictionary with the same keys, but with the values multiplied by 2. The new dictionary should only include the keys from the original dictionary that have a value greater than 5.
"""

def multiply_values(input_dict):
    """
    Returns a new dictionary with the same keys, but with the values multiplied by 2.
    The new dictionary only includes the keys from the original dictionary that have a value greater than 5.

    Args:
        input_dict (dict): The input dictionary.

    Returns:
        dict: A new dictionary with the values multiplied by 2.
    """
    return {key: value*2 for key, value in input_dict.items() if value > 5}