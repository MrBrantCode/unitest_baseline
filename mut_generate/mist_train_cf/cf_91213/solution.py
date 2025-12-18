"""
QUESTION:
Write a function called `access_nested_value` that takes a dictionary as input, where the dictionary contains a key 'nested_list' that maps to a list containing another dictionary. The inner dictionary has a key 'name' with a string value. The function should return the value of the key 'name'. Assume the list contains only one dictionary.
"""

def access_nested_value(input_dict):
    return input_dict['nested_list'][0]['name']