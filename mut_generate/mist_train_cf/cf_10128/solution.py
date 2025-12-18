"""
QUESTION:
Access the value of a key in a nested dictionary within a list. 

Write a function `access_nested_key` that takes a dictionary as input where the dictionary contains a key 'nested_list' that maps to a list of dictionaries. Each dictionary in the list has a key 'name'. The function should return the value of 'name' in the first dictionary of the list.
"""

def access_nested_key(input_dict):
    """
    This function accesses the value of the key 'name' in the first dictionary 
    of the list mapped to the key 'nested_list' in the input dictionary.
    
    Args:
        input_dict (dict): A dictionary containing a key 'nested_list' that maps to a list of dictionaries.
        
    Returns:
        str: The value of 'name' in the first dictionary of the list.
    """
    return input_dict['nested_list'][0]['name']