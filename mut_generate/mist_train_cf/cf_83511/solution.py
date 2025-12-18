"""
QUESTION:
Write a function `to_json(nested_dict, indent=0)` that transforms the key-value pairs of a nested dictionary into a structured JSON string without using any external library. The function should return a string formatted as a JSON object and handle both simple dictionary pairs and nested ones.
"""

def to_json(nested_dict, indent=0):
    json_str = '{\n'
    for i, (key, value) in enumerate(nested_dict.items()):
        json_str += ' ' * (indent + 4) + f'"{key}": '
        if isinstance(value, dict):
            json_str += to_json(value, indent + 4)
        else:
            json_str += f'"{value}"'
        if i < len(nested_dict) - 1:
            json_str += ',\n'
        else:
            json_str += '\n'
    json_str += ' ' * indent + '}'
    return json_str