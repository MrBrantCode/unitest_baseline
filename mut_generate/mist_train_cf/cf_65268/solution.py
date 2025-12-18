"""
QUESTION:
Create a function named `check_empty_dict` that checks if a dictionary and all its nested dictionaries are empty, and returns a tuple. The first element of the tuple should be a boolean indicating whether the main dictionary and all its nested dictionaries are empty, and the second element should be an integer representing the total number of empty dictionaries. The function should handle circular references, and also check for emptiness of lists, tuples, and sets nested within the dictionaries.
"""

def check_empty_dict(nested_dict):
    empty_dict_count = 0
    non_empty_dict_found = False
    checked_objects = set()

    def _check_empty(obj):
        nonlocal empty_dict_count, non_empty_dict_found

        # If the object has been checked before, return immediately
        if id(obj) in checked_objects:
            return

        checked_objects.add(id(obj))

        # If the object is a dictionary
        if isinstance(obj, dict):
            if len(obj) == 0:
                empty_dict_count += 1
            else:
                for v in obj.values():
                    _check_empty(v)
                if len(obj) > 0:
                    non_empty_dict_found = True

        # If the object is a list, tuple, or set
        elif isinstance(obj, (list, tuple, set)):
            for item in obj:
                _check_empty(item)

    _check_empty(nested_dict)

    return not non_empty_dict_found, empty_dict_count