"""
QUESTION:
Write a function `ConvertDictionaryToJSON` that takes a dictionary as input and returns a JSON string representation of the dictionary. The function should exclude any empty dictionaries from the output and handle nested dictionaries.
"""

import json

def ConvertDictionaryToJSON(dictionary):
    def ConvertToJSONString(value):
        if isinstance(value, dict):
            return ConvertDictionaryToJSON(value)
        else:
            return json.dumps(value)

    result = []
    for key, value in dictionary.items():
        if isinstance(value, dict):
            nested_json = ConvertDictionaryToJSON(value)
            if nested_json != '{}':
                result.append(f'"{key}":{nested_json}')
        else:
            result.append(f'"{key}":{ConvertToJSONString(value)}')

    return '{' + ','.join(result) + '}'