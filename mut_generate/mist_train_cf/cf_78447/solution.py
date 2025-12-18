"""
QUESTION:
Create a function `merge_and_filter` that takes two dictionaries `dict1` and `dict2`, and a list of keys. The function should merge `dict1` and `dict2` into a new dictionary, with values from `dict2` overriding those from `dict1` in case of duplicate keys. Then, it should return a dictionary containing only the key-value pairs from the merged dictionary where the keys are present in the provided list.
"""

def merge_and_filter(dict1, dict2, keys):
    merged_dict = {**dict1, **dict2}
    return {key: merged_dict[key] for key in keys if key in merged_dict}