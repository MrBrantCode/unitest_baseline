"""
QUESTION:
Create a function named `to_dict` that takes two lists as input, `list1` and `list2`. The function should return a dictionary where elements from `list1` are used as keys and elements from `list2` are used as values. If a duplicate key is encountered, the corresponding value should be appended to a list. The function should handle cases where the key already has a single value or a list of values. The input lists are assumed to be of the same length.
"""

def to_dict(list1, list2):
    result = {}
    for key, value in zip(list1, list2):
        if key in result:
            if type(result[key]) == list:
                result[key].append(value)
            else:
                result[key] = [result[key], value]
        else:
            result[key] = value
    return result