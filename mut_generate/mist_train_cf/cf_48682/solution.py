"""
QUESTION:
Implement a function `check_empty_dicts` that takes an input dictionary and returns a tuple containing a boolean indicating whether the dictionary is not empty and the total number of empty dictionaries (including the input dictionary) in the dictionary tree. The function should handle nested dictionaries, lists, tuples, and sets. It should not count a dictionary as empty if it contains non-empty dictionaries. If the dictionary is empty or contains only empty dictionaries, return `(False, total_empty)`, otherwise return `(True, total_empty)`.
"""

def check_empty_dicts(input_dict):
    # Track dictionary references to prevent infinite loops
    seen_dicts = set()
    total_empty = 0   
    not_empty = False

    def recurse_dict(dic):
        nonlocal total_empty, not_empty
        if id(dic) in seen_dicts:
            # Skip if already seen this dictionary to prevent infinite loops
            return
        seen_dicts.add(id(dic))
        for k, v in dic.items():
            if isinstance(v, dict):
                if len(v) == 0:
                    total_empty += 1
                else:
                    recurse_dict(v)
            elif isinstance(v, (list, tuple, set)):
                for i in v:
                    if isinstance(i, dict):
                        if len(i) == 0:
                            total_empty += 1
                        else:
                            recurse_dict(i)
        if len(dic) != 0:
            not_empty = True

    recurse_dict(input_dict)

    return (not_empty, total_empty)