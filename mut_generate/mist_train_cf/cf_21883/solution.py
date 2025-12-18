"""
QUESTION:
Write a function named `update_json_object` that takes a nested JSON object, a target key, and two source keys as input. The function should modify the JSON object in-place by updating the value of the second source key in the target key's sub-object to be the sum of the values of the two source keys. The function should return the modified JSON object. If the target key or either of the source keys are not present in the JSON object, the function should raise an exception. The time complexity of the function should be O(n), where n is the number of keys in the JSON object.
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