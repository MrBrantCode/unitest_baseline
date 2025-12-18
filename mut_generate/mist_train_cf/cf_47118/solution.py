"""
QUESTION:
Generate a function `generate_dicts` that takes two parameters: an integer `n` and an optional list of keys. The function should return a list of `n` dictionaries. Each dictionary should have a unique identifier as key and an empty dictionary as its value. 

If the list of keys is provided, use these keys as identifiers for the dictionaries, ignoring any duplicates. If the list of keys is shorter than `n`, generate unique identifiers for the remaining dictionaries. The returned list of dictionaries should maintain the order of the keys as they were provided in the list, or the order they were created if no list was provided.
"""

def generate_dicts(n, keys=None):
    result = [{} for _ in range(n)]
    identifiers = set()

    if keys is not None:
        for i, key in enumerate(keys):
            if key not in identifiers and i < n:
                result[i] = { key: {} }
                identifiers.add(key)

    remaining = n - len(identifiers)
    i = 0

    for dictionary in result:
        if not dictionary:
            unique_id = str(i)
            while unique_id in identifiers:
                i += 1
                unique_id = str(i)
            dictionary.update({unique_id: {}})
            identifiers.add(unique_id)
            i += 1

    return result