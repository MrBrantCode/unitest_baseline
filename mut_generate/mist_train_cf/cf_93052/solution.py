"""
QUESTION:
Write a function named `update_json` that takes in a JSON object and three keys as input: `key`, `key1`, and `key2`. The function should update the value of `key` to the sum of the values of `key1` and `key2` in the JSON object, and return the modified object. If `key`, `key1`, or `key2` is not present in the JSON object, the function should raise an exception. The function must have a time complexity of O(n), where n is the number of keys in the JSON object.
"""

def update_json(json_obj, key, key1, key2):
    if key not in json_obj or key1 not in json_obj or key2 not in json_obj:
        raise Exception("Specified key or the two other keys are not present in the JSON object")
    
    json_obj[key] = json_obj[key1] + json_obj[key2]
    return json_obj