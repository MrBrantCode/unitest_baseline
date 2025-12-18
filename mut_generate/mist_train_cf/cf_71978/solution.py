"""
QUESTION:
Create a function called `reverse_and_sort_dict` that takes a dictionary as input, reverses its key-value pairs, and returns a new dictionary where the keys (which are the original values) are sorted in descending alphabetical order.
"""

def reverse_and_sort_dict(input_dict):
    """
    Reverses key-value pairs in a dictionary and returns a new dictionary 
    where the keys (which are the original values) are sorted in descending alphabetical order.
    
    Args:
        input_dict (dict): The input dictionary.
    
    Returns:
        dict: A new dictionary with reversed key-value pairs and sorted keys.
    """
    # reverse keys and values
    reversed_dict = {value: key for key, value in input_dict.items()}
    
    # sort keys in descending order and create a new dictionary
    sorted_dict = {key: reversed_dict[key] for key in sorted(reversed_dict, reverse=True)}
    
    return sorted_dict