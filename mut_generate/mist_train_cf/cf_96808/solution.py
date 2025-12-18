"""
QUESTION:
Write a function `update_json_object` that takes in a nested JSON object and three keys as input: `target_key`, `source_key1`, and `source_key2`. The function should update the value of `source_key2` under `target_key` to be the sum of the values of `source_key1` and `source_key2` under `target_key`. The function should have a time complexity of O(n), where n is the number of keys in the JSON object. If `target_key`, `source_key1`, or `source_key2` are not present in the JSON object, the function should raise an exception. The function should modify the input JSON object in-place and return the modified object.
"""

def update_json_object(json_object, target_key, source_key1, source_key2):
    # Check if target key exists
    if target_key not in json_object:
        raise Exception(f"Target key '{target_key}' not found in JSON object")
    
    # Check if source keys exist
    if source_key1 not in json_object[target_key] or source_key2 not in json_object[target_key]:
        raise Exception(f"One or both source keys '{source_key1}' and '{source_key2}' not found in JSON object")
    
    # Update the value of the target key
    json_object[target_key][source_key2] = json_object[target_key][source_key1] + json_object[target_key][source_key2]
    
    return json_object