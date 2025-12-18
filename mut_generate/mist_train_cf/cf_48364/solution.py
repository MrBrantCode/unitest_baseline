"""
QUESTION:
Create a function `find_key` that takes a dictionary `nested_dict` and a `target_key` as arguments. The function should be able to extract the value(s) corresponding to the `target_key` from any level of nesting within the dictionary. If the same `target_key` is present at multiple levels, the function should return all corresponding values. If the `target_key` is not found within the dictionary, the function should return `None`. The function should also handle InterruptedErrors in a graceful manner.
"""

def find_key(nested_dict, target_key):
    results = []
    try:
        for key, value in nested_dict.items():
            if key == target_key:
                results.append(value)
            if isinstance(value, dict):
                results += find_key(value, target_key)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        results += find_key(item, target_key)
        return results if results else None
    except InterruptedError:
        return None