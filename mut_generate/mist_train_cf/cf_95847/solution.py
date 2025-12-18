"""
QUESTION:
Write a function `flatten_dictionary` that takes a dictionary as input and returns a flattened dictionary. The input dictionary may contain nested dictionaries of arbitrary depth with string keys and values of string, integer, or boolean types. The keys of the output dictionary should be in the format "parentkey_childkey" for nested keys. The function should have a time complexity of O(n), where n is the total number of elements in the input dictionary.
"""

def flatten_dictionary(d):
    def flatten_helper(item, prefix=''):
        if isinstance(item, dict):
            flattened_dict = {}
            for key, value in item.items():
                new_key = prefix + key if prefix else key
                flattened_dict.update(flatten_helper(value, new_key + '_'))
            return flattened_dict
        else:
            return {prefix[:-1]: item}

    return flatten_helper(d)