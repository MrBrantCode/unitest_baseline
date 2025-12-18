"""
QUESTION:
Create a function `find_key` that takes a nested structure (`input_structure`) and a target key (`target_key`) as input. The function should recursively traverse the structure and return the path to `target_key` whenever it appears. The function should also count the total occurrences of `target_key` and handle different types of nested structures such as lists, tuples, and dictionaries. If `target_key` is not found, the function should return the appropriate response. The function should not be designed to handle circular references.
"""

def find_key(input_structure, target_key, path=None):
    if path is None:
        path = []

    if isinstance(input_structure, dict):
        iterator = input_structure.items()
    elif isinstance(input_structure, (list, tuple)):
        iterator = enumerate(input_structure)
    else:
        return

    for key, value in iterator:
        new_path = list(path)
        new_path.append(key)

        if value == target_key:
            yield (new_path, 1)
        elif isinstance(value, (dict, list, tuple)):
            for result in find_key(value, target_key, new_path):
                yield result
        elif value == target_key:
            yield (new_path, 1)