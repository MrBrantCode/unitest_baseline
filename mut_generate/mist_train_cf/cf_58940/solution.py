"""
QUESTION:
Create a function named `merge_dicts` that merges two dictionaries. The function should handle overlapping keys by checking if their values are dictionaries or lists and merging them accordingly. If the values are dictionaries, the function should call itself recursively. If the values are lists, the lists should be concatenated. If the values are of any other type, they should be placed in a list. The function should modify the first dictionary in-place and return it.
"""

def merge_dicts(dict1, dict2):
    for key in dict2:
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                merge_dicts(dict1[key], dict2[key])
            elif dict1[key] == dict2[key]:
                pass # same leaf value
            else:
                if isinstance(dict1[key], list):
                    if isinstance(dict2[key], list):
                        dict1[key].extend(dict2[key])
                    else:
                        dict1[key].append(dict2[key])
                else:
                    if isinstance(dict2[key], list):
                        dict2[key].append(dict1[key])
                        dict1[key] = dict2[key]
                    else:
                        dict1[key] = [dict1[key], dict2[key]]
        else:
            dict1[key] = dict2[key]
    return dict1