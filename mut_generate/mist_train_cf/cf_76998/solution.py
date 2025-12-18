"""
QUESTION:
Implement a function `process_nested_dict` that takes a dictionary `d` as input and processes its elements. The function should handle dictionaries with variable levels of nesting, where each value can be a string, integer, or another dictionary. The function should multiply each integer by its order of discovery and concatenate each string to a growing string. The function should return the modified dictionary and the final string.
"""

def process_nested_dict(d, order=1, string=''):
    result = {}
    for k, v in d.items():
        if isinstance(v, dict):
            v, order, string = process_nested_dict(v, order, string)
        elif isinstance(v, int):
            v *= order
            order += 1
        elif isinstance(v, str):
            string += v
        result[k] = v
    return result, order, string