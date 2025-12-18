"""
QUESTION:
Write a function `convert_to_json` that takes a dictionary as input and returns a valid JSON string representation of the dictionary. The function should handle integers, floats, booleans, strings, lists, and nested dictionaries. The JSON string should be properly indented and formatted, with keys sorted alphabetically in a case-sensitive manner. Any non-string keys should be converted to strings, and any non-string values should be converted to their corresponding JSON representations. The function should not use any built-in JSON conversion methods or libraries and should handle circular references in the dictionary, raising an exception if one is found. The function should have a time complexity of O(n), where n is the total number of elements in the dictionary.
"""

def convert_to_json(data):
    def check_circular_reference(data, path=[]):
        if isinstance(data, dict):
            if id(data) in path:
                raise Exception("Circular reference found!")
            path.append(id(data))
            for value in data.values():
                check_circular_reference(value, path)
            path.pop()
        elif isinstance(data, list):
            for item in data:
                check_circular_reference(item, path)
    
    check_circular_reference(data)
    
    def convert_value(value):
        if isinstance(value, int) or isinstance(value, float) or isinstance(value, bool):
            return str(value).lower()
        elif isinstance(value, str):
            return f'"{value}"'
        elif isinstance(value, list):
            return convert_list(value)
        elif isinstance(value, dict):
            return convert_dict(value)
    
    def convert_list(lst):
        elements = []
        for item in lst:
            elements.append(convert_value(item))
        return "[" + ", ".join(elements) + "]"
    
    def convert_dict(dct):
        elements = []
        for key, value in sorted(dct.items()):
            if not isinstance(key, str):
                key = str(key)
            elements.append(f'"{key}": {convert_value(value)}')
        return "{" + ", ".join(elements) + "}"
    
    return convert_dict(data)