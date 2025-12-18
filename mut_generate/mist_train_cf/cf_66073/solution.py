"""
QUESTION:
Implement a function `extract_values(json_obj, target_key)` that extracts the value(s) of a nested key `target_key` from a JSON object `json_obj`. The function should:

* Return the value if the key exists only once.
* Return a list of values if the key exists multiple times.
* Return "Key not found" or an empty list if the key does not exist.
* Detect and handle cycles in the JSON object to prevent infinite recursion.

The JSON object can have multiple nested keys of unknown depth, and the function should be able to traverse it recursively.
"""

def extract_values(json_obj, target_key, visited=None):
    if visited is None:
        visited = set()
    if id(json_obj) in visited:
        return []
    visited.add(id(json_obj))
    
    result = []
    for key, value in json_obj.items():
        if key == target_key:
            result.append(value)
        if isinstance(value, dict):
            result.extend(extract_values(value, target_key, visited))
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    result.extend(extract_values(item, target_key, visited))
    return result