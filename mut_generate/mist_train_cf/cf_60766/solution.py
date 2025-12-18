"""
QUESTION:
Write a function `check_dict_sorting(d)` that checks if a given dictionary `d` is sorted and determines the nature of the sorting (alphabetical or reverse alphabetical). The function should handle dictionaries containing various data types as keys or values and be able to manage exceptions or errors. It should also handle nested dictionaries, returning a dictionary where each key is the key of the nested dictionary and the value is the sorting order of that nested dictionary. If the dictionary is not sorted, the function should return 'unsorted'.
"""

from typing import Any, Dict

def check_dict_sorting(d: Dict[Any, Any]):
    """Check the sorting order of a dictionary and its nested dictionaries"""
    def is_sorted(iterable, reverse=False):
        """Check if an iterable is sorted"""
        iterable = list(iterable)
        return iterable == sorted(iterable, reverse=reverse)

    def determine_sorting(d: Dict[Any, Any]):
        """Determine sorting order of a dictionary"""
        keys = list(d.keys())
        if is_sorted(keys):
            return 'alphabetical'
        elif is_sorted(keys, True):
            return 'reverse alphabetical'
        else:
            return 'unsorted'

    results = {}
    for key, value in d.items():
        if isinstance(value, dict):
            result = determine_sorting(value)
            results[key] = result
        else:
            result = determine_sorting(d)
            results['main'] = result
            break
    return results