"""
QUESTION:
Write a function `convert_to_dict` that takes a nested array as input, where each subarray contains a pair of keys and associated values. This function should convert this data structure into a nested dictionary, merging dictionaries and appending new values into an array when the same key appears in multiple subarrays, while maintaining the original keys.
"""

def convert_to_dict(nested_array):
    result_dict = {}
    for sub_array in nested_array:
        for pair in sub_array:
            key, value = pair
            if key in result_dict:
                if isinstance(result_dict[key], list):
                    result_dict[key].append(value)
                else:
                    result_dict[key] = [result_dict[key], value]
            else:
                result_dict[key] = value
    return result_dict