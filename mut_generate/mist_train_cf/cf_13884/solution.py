"""
QUESTION:
Create a function named `update_dict_item` that takes in three parameters: a dictionary, a key, and a value. The function should return a new dictionary with the updated values without modifying the original dictionary. The function should handle the following scenarios: 

- If the key exists in the dictionary, update its value with the given value. 
- If the existing value and the new value are both lists or dictionaries, update the nested values recursively. 
- If the existing value and the new value have different data types, update the value accordingly. 
- If the key does not exist in the dictionary, add it with the corresponding value.
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