"""
QUESTION:
Implement a Python function `_backwardCompat` that takes a JSON object `result_json` as input. The function should recursively process the input JSON object, applying the following transformation rules to the keys:
- If a key's value is a dictionary, convert the key to lowercase and recursively apply the transformation to the nested dictionary.
- If a key is 'Token', replace it with 'sessionToken'.
- For all other keys, convert the first letter to lowercase.
The function should return the transformed JSON object in a backward-compatible format.
"""

def entrance(result_json):
    bc_json = dict()
    for k, v in result_json.items():
        if isinstance(v, dict):
            bc_json[k[0].lower() + k[1:]] = entrance(v)
        elif k == 'Token':
            bc_json['sessionToken'] = v
        else:
            bc_json[k[0].lower() + k[1:]] = v
    return bc_json