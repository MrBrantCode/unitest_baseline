"""
QUESTION:
Design a function `transform_tuple_to_dict` that transforms a tuple of strings into a dictionary. Each string in the tuple is formatted as "key: value" where the key can be a nested key formatted as "key1.key2.key3" and the value can be a single value or a list of values formatted as "value1, value2, value3". The function should return a dictionary where the nested keys are represented as nested dictionaries and the values are either single values or lists of values.
"""

def transform_tuple_to_dict(tup):
    dict_result = {}
    
    # iterate over each element in the tuple
    for item in tup:
        # split each item by ': ' to define key and value
        item_parts = item.split(': ')
        key_parts = item_parts[0].split('.')
        
        # define last_dict to keep track of the nested dictionary
        last_dict = dict_result

        # iterate over each part of the key and update the dictionary
        for part in key_parts[:-1]:
            if part not in last_dict:
                last_dict[part] = {}
            last_dict = last_dict[part]
        
        # set the value to the deepest key
        value_parts = item_parts[1].split(', ')
        last_dict[key_parts[-1]] = value_parts if len(value_parts) > 1 else value_parts[0]
        
    return dict_result