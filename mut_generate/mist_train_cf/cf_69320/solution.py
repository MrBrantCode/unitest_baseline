"""
QUESTION:
Develop a recursive function named `get_values` that retrieves the values of specific keys from a deeply nested JSON object. The function should accept a JSON object and a list of keys as parameters, and return a dictionary containing the values of the specified keys. If a specified key is absent in the JSON data, the function should return 'Key not present in JSON data' for that key. The function should be designed to accommodate additional depth of layers in the JSON data without necessitating alterations to the function.
"""

def get_values(json_obj, keys):
    """Recursive function to get values of keys in a nested JSON"""
    result = {}

    def helper(obj):
        if isinstance(obj, dict):
            for key in obj:
                if key in keys:
                    result[key] = obj[key]
                helper(obj[key])
        elif isinstance(obj, list):
            for item in obj:
                helper(item)

    helper(json_obj)

    missing_keys = set(keys) - set(result.keys())
    for missing_key in missing_keys:
        result[missing_key] = 'Key not present in JSON data'

    return result