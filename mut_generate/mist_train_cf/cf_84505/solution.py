"""
QUESTION:
Create a function named `multiply_dicts` that takes two dictionaries `d1` and `d2` as input. The function should return a new dictionary where each key-value pair from `d1` is multiplied by the corresponding value in `d2`, if it exists. If a key in `d1` does not exist in `d2`, its value in the output dictionary should remain unchanged. The function should also handle nested dictionaries, where the values of `d1` and `d2` can be dictionaries themselves. If a value in `d1` is a dictionary, the function should recursively multiply its values with the corresponding values in `d2`. The function should not modify the original dictionaries and should raise no exceptions.
"""

def multiply_dicts(d1, d2):
    result = {}
    for key in d1:
        if isinstance(d1[key], dict):
            if key in d2 and isinstance(d2[key], dict):
                result[key] = multiply_dicts(d1[key], d2[key])
            else:
                result[key] = d1[key]
        else:
            if key in d2 and not isinstance(d2[key], dict):
                result[key] = d1[key] * d2[key]
            else:
                result[key] = d1[key]
    return result