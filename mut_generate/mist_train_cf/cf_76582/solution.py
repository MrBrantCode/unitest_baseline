"""
QUESTION:
Create a function `inverse_dict_sort` that takes a dictionary as input, reverses the key-value pairs, and returns the resulting dictionary sorted in descending order by the new keys (alphanumeric standards). The function should handle dictionaries with string values.
"""

def inverse_dict_sort(my_dict):
    """
    This function takes a dictionary as input, reverses the key-value pairs, 
    and returns the resulting dictionary sorted in descending order by the new keys.
    
    Args:
        my_dict (dict): The input dictionary with string values.
    
    Returns:
        dict: The resulting dictionary with reversed key-value pairs, sorted in descending order.
    """
    # Inverse the keys and values of the dictionary
    inv_dict = {v: k for k, v in my_dict.items()}
    # Sort the inverted dictionary by values in descending order
    sorted_dict = dict(sorted(inv_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict