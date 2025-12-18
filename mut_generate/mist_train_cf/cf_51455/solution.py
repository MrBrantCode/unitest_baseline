"""
QUESTION:
Write a function `analyze_dict(input_dict)` that takes one argument: a dictionary. 

The function should do the following: 
- Check if the input is a dictionary, raise an exception if not.
- Check if the dictionary is empty, return a message if so.
- Count the number of entries in the dictionary.
- Count the number of nested dictionaries in the dictionary.
- Count the occurrences of each type of value in the dictionary, including nested dictionaries.
- Return a dictionary with the counts of each type of value.

The function should handle exceptions properly and provide clear error messages.
"""

def analyze_dict(input_dict):
    # define a dictionary to store types and their count
    type_freq = {}
    
    if not isinstance(input_dict, dict):
        raise Exception('The argument passed is not a dictionary')
    elif not input_dict:
        return 'The dictionary is empty'
    else:
        # track the count of dictionary entries
        entry_count = 0

        # track the count of nested dictionaries
        nested_dict_count = 0

        for val in input_dict.values():
            # if the value is a nested dictionary
            if isinstance(val, dict):
                nested_dict_count += 1
                for nested_val in val.values():
                    # add the type to the dictionary with a count
                    nested_val_type = type(nested_val)
                    if nested_val_type not in type_freq:
                        type_freq[nested_val_type] = 1
                    else:
                        type_freq[nested_val_type] += 1
            else:
                # add the type to the dictionary with a count
                val_type = type(val)
                if val_type not in type_freq:
                    type_freq[val_type] = 1
                else:
                    type_freq[val_type] += 1
            entry_count += 1

        # update the dictionary to contain counts using type names
        type_freq = {str(k): v for k, v in type_freq.items()}
        type_freq['entry_count'] = entry_count
        type_freq['nested_dict_count'] = nested_dict_count

        return type_freq