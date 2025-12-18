"""
ORIGINAL QUESTION:
Write a function called `get_even_keys_in_reverse` that takes a dictionary as input and returns a list of keys with even values in the reverse order they were added. The function should work in Python 3.7 and later versions, utilizing the fact that dictionaries maintain the insertion order.
"""

def get_even_keys_in_reverse(input_dict):
    """
    Returns a list of keys with even values in the reverse order they were added.
    
    Args:
    input_dict (dict): The input dictionary.
    
    Returns:
    list: A list of keys with even values in the reverse order.
    """
    return list(reversed([key for key, value in input_dict.items() if value % 2 == 0]))