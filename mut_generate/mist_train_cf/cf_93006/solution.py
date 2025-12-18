"""
QUESTION:
Create a function `update_dict_item` that updates the existing item of a dictionary with a new value. The function should not modify the original dictionary but instead return a new dictionary with the updated values. 

The function should handle the following scenarios:
- If the key exists in the dictionary and the new value is of a different data type, the function should update the value accordingly.
- If the key exists in the dictionary and the new value is a list or a dictionary, the function should recursively check for any nested values and update them as well.
- If the key does not exist in the dictionary, the function should add it with the corresponding value. 

The function should take three parameters: the dictionary to be updated, the key to be updated, and the new value.
"""

def update_dict_item(dictionary, key, value):
    new_dict = dictionary.copy()  # create a new dictionary to hold the updated values
    
    if key in new_dict:
        # if the key exists in the dictionary
        
        if type(value) in [list, dict] and type(new_dict[key]) in [list, dict]:
            # if both the existing value and the new value are of list or dict type,
            # recursively update the nested values
            
            if isinstance(new_dict[key], list) and isinstance(value, list):
                # if both the existing value and the new value are lists, update the list
                new_dict[key] = value
            elif isinstance(new_dict[key], dict) and isinstance(value, dict):
                # if both the existing value and the new value are dictionaries, update the dictionary
                for sub_key, sub_value in value.items():
                    new_dict[key][sub_key] = sub_value
        else:
            # if the existing value and the new value have different data types, update the value
            new_dict[key] = value
    else:
        # if the key does not exist in the dictionary, add it with the corresponding value
        new_dict[key] = value
    
    return new_dict