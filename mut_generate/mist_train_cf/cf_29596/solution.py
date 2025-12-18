"""
QUESTION:
Implement a function `compare_elements` that compares two elements `el1` and `el2` of any data type (strings, numbers, lists, tuples, sets, dictionaries) and returns `True` if they are equal, `False` otherwise. 

For strings, the comparison should replace values based on the `replace_list` using the `_replace` function. For lists, tuples, and sets, the comparison should be recursive. For dictionaries, the comparison should be recursive for both keys and values. 

The function should handle different data types and lengths, and return `False` for unsupported data types.
"""

def compare_elements(el1, el2, replace_list=[("old_value", "new_value")]):
    def _replace(s):
        if s is None:
            return ''
        _s = s
        for u, v in replace_list:
            _s = _s.replace(u, v)
        return _s

    if type(el1) != type(el2):
        return False
    if isinstance(el1, str):
        return _replace(el1) == _replace(el2)
    elif isinstance(el1, (int, float, bool)):
        return el1 == el2
    elif isinstance(el1, (list, tuple, set)):
        if len(el1) != len(el2):
            return False
        for e1, e2 in zip(el1, el2):
            if not compare_elements(e1, e2, replace_list):
                return False
        return True
    elif isinstance(el1, dict):
        if len(el1) != len(el2):
            return False
        for k1, v1 in el1.items():
            if k1 not in el2 or not compare_elements(v1, el2[k1], replace_list):
                return False
        return True
    else:
        return False