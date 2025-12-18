"""
QUESTION:
Create a function called `merge_objects` that takes two dictionaries `a` and `b` as parameters. The function should merge the two dictionaries into a single dictionary, where the keys from both input dictionaries are included and in case of duplicate keys, the value from the second dictionary overwrites the value from the first dictionary. The merged dictionary should only include keys that consist of alphabetic characters (A-Z, a-z) and exclude any keys that contain non-alphabetic characters. The function should handle nested dictionaries within the input dictionaries and merge them accordingly. The merged dictionary should be sorted in descending order based on the keys.
"""

def merge_objects(a, b):
    merged = {}
  
    def merge_nested(merged, key, nested):
        if key not in merged:
            merged[key] = {}
        for nested_key, nested_value in nested.items():
            if isinstance(nested_value, dict):
                merge_nested(merged[key], nested_key, nested_value)
            elif nested_key.isalpha():
                merged[key][nested_key] = nested_value
  
    for key, value in a.items():
        if isinstance(value, dict):
            merge_nested(merged, key, value)
        elif key.isalpha():
            merged[key] = value
  
    for key, value in b.items():
        if isinstance(value, dict):
            merge_nested(merged, key, value)
        elif key.isalpha():
            merged[key] = value
  
    return dict(sorted(merged.items(), key=lambda item: item[0], reverse=True))