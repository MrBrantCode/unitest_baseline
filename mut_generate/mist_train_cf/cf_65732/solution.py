"""
QUESTION:
Write a Python function named `flatten` that takes in an object and returns a flattened list of its elements. The object can be a list, set, tuple, or dictionary. If the object is a dictionary, recursively flatten its keys and values. If the object is not one of the above types, treat it as a single element list.

Write a Python function named `identify` that takes in a set of keys and a dictionary of two dictionaries. The dictionaries have the keys from the set and their corresponding counts as values. The function should return a dictionary where the keys are the unique elements from the set and the values are lists containing the count of the element in the first dictionary, the count of the element in the second dictionary, and a string indicating whether the element is present in both dictionaries or not.

Write a Python function named `comparison` that takes in two tuples and returns the non-identical elements and their frequencies. The function should first flatten the tuples using the `flatten` function, then count the frequency of each element in the flattened tuples. It should then call the `identify` function to get the non-identical elements and their frequencies.
"""

def flatten(obj):
    """
    Flatten complex data types including list, set, dict or tuple into a list. 
    """
    result = []
    if isinstance(obj, (list, set, tuple)):
        for element in obj:
            result.extend(flatten(element))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            result.extend(flatten(k))
            result.extend(flatten(v))
    else:
        result.append(obj)
    return result

def identify(keys, dicts):
    """
    Identify the non-identical elements and quantify the frequency, 
    """
    result = {}
    for key in keys:
        if isinstance(key, tuple):
            key = flatten(key)
        if key in dicts['tuple1']:
            if key in dicts['tuple2']:
                result[str(key)] = [dicts['tuple1'][key], dicts['tuple2'][key], 'both']
            else:
                result[str(key)] = [dicts['tuple1'][key], 0, 'tuple1']
        else:
            result[str(key)] = [0, dicts['tuple2'][key], 'tuple2']
    return result

def comparison(tuple1, tuple2):
    """
    Compare two tuples and return the non-identical elements,
    """
    flattened_tuple1 = flatten(tuple1)
    flattened_tuple2 = flatten(tuple2)

    count_dict1 = {i: flattened_tuple1.count(i) for i in flattened_tuple1}
    count_dict2 = {i: flattened_tuple2.count(i) for i in flattened_tuple2}

    all_keys = set(list(count_dict1.keys()) + list(count_dict2.keys()))

    dicts = {
        'tuple1': count_dict1,
        'tuple2': count_dict2
    }

    result = identify(all_keys, dicts)

    return result