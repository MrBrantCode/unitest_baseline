"""
QUESTION:
Write a function named `update_json` that takes a JSON object, and three keys as input. The function should modify the JSON object in-place by updating the value of the first key to the sum of the values of the other two keys. The function should return the modified JSON object. If any of the specified keys are not present in the JSON object, the function should raise an exception.
"""

def update_json(json_obj, key, key1, key2):
    if key not in json_obj or key1 not in json_obj or key2 not in json_obj:
        raise Exception("Specified key or the two other keys are not present in the JSON object")
    
    json_obj[key] = json_obj[key1] + json_obj[key2]
    return json_obj