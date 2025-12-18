"""
QUESTION:
Write a function `analyze_dicts(obj, seen=None)` that takes an object `obj` and an optional set `seen` as input, and returns a tuple of three values: a boolean indicating whether `obj` is a void dictionary, the total number of void dictionaries found, and the total number of keys found. The function should recursively traverse `obj` and its nested objects, handling circular references, dictionaries, and other iterable types. If `obj` is a dictionary, it should count the number of void dictionaries and keys within it. If `obj` is not a dictionary, it should return False with zero counts for void dictionaries and total keys.
"""

def analyze_dicts(obj, seen=None):
    if seen is None:
        seen = set()

    if id(obj) in seen:
        return False, 0, 0  

    seen.add(id(obj))

    if isinstance(obj, dict):
        if not obj:
            return True, 1, 0  
        else:
            total_voids = total_keys = 0
            for key, val in obj.items():
                is_void, num_voids, num_keys = analyze_dicts(val, seen)
                total_keys += num_keys  
                if is_void:
                    total_voids += num_voids  
                total_keys += 1  
            return False, total_voids, total_keys  
    elif isinstance(obj, (list, tuple, set)):  
        total_voids = total_keys = 0
        for item in obj:
            is_void, num_voids, num_keys = analyze_dicts(item, seen)
            total_voids += num_voids
            total_keys += num_keys
        return False, total_voids, total_keys  
    else:  
        return False, 0, 0  