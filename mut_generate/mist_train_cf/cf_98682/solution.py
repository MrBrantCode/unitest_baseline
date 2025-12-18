"""
QUESTION:
Create a function called `create_new_dict` that takes a nested dictionary as input. The function should return a new dictionary where the key is the value of the "name" key and the value is the value of the "needed_value" key in the nested dictionary.
"""

def create_new_dict(nested_dict):
    return {v['name']: v['needed_value'] for k, v in nested_dict.items()}