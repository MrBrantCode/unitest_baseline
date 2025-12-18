"""
QUESTION:
Create a function named `sort_dict_by_value` that takes a dictionary as input, filters it to include only keys that start with a lowercase letter and end with an uppercase letter, and values that are divisible by 3. The function should return a new dictionary sorted by values in ascending order. The original dictionary should remain unchanged.
"""

def sort_dict_by_value(input_dict):
    """
    This function filters a dictionary to include only keys that start with a lowercase letter and end with an uppercase letter,
    and values that are divisible by 3. It returns a new dictionary sorted by values in ascending order.

    Args:
        input_dict (dict): The input dictionary.

    Returns:
        dict: A new dictionary sorted by values in ascending order.
    """
    return {k: v for k, v in sorted(
        {key: value for key, value in input_dict.items() if value % 3 == 0 and key[0].islower() and key[-1].isupper()}.items(), 
        key=lambda item: item[1]
    )}