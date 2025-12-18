"""
QUESTION:
Write a function named `find_keys` that accepts two parameters: `json_data` (a JSON object) and `keys` (a list of key names). The function should recursively search through `json_data` to find all values of keys named in the `keys` list, handling potential errors and nested JSON objects or arrays. The function should return a list of all found values.
"""

def find_keys(json_data, keys):
    results = []

    def _extract_items(obj, keys, results):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key in keys:
                    results.append(value)
                if isinstance(value, (dict, list)):
                    _extract_items(value, keys, results)
        elif isinstance(obj, list):
            for item in obj:
                _extract_items(item, keys, results)

    _extract_items(json_data, keys, results)
    
    return results