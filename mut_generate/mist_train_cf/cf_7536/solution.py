"""
QUESTION:
Create a function `someFunction` that takes an array of objects as input. The function should return an array of strings, where each string consists of the keys and values from each object in the input array. The function should ignore any objects that have a key called "ignore" and should only consider objects that have at least two key-value pairs. If an object contains a nested object, the function should also include the keys and values from the nested object in the resulting string. The function should support nested objects of arbitrary depth.
"""

def someFunction(arr):
    result = []
    
    for obj in arr:
        if 'ignore' in obj or len(obj) < 2:
            continue
        
        str = ''
        count = 0
        
        for key, value in obj.items():
            if key == 'ignore':
                continue
            
            if isinstance(value, dict):
                for nested_key, nested_value in flatten_dict(value).items():
                    count += 1
                    str += f"{key}.{nested_key} is {nested_value}, "
            else:
                count += 1
                str += f"{key} is {value}, "
        
        if count < 2:
            continue
        
        result.append(str[:-2])  # remove trailing comma and space
    
    return result


def flatten_dict(nested_dict, prefix=''):
    flat_dict = {}
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            flat_dict.update(flatten_dict(value, prefix + key + '.'))
        else:
            flat_dict[prefix + key] = value
    return flat_dict