"""
QUESTION:
Implement a function `is_recursive_subnamespace(namespace, parent_namespace)` that checks if `namespace` is a recursive subnamespace of `parent_namespace`. The function should return `True` if all attributes and sub-namespaces of `namespace` are present in `parent_namespace` with the same values, and `False` otherwise. The function should handle nested namespaces of arbitrary depth.
"""

def entrance(namespace, parent_namespace):
    if not isinstance(namespace, dict) or not isinstance(parent_namespace, dict):
        return False

    for key, value in namespace.items():
        if key not in parent_namespace:
            return False
        if isinstance(value, dict):
            if not entrance(value, parent_namespace[key]):
                return False
        elif value != parent_namespace[key]:
            return False

    return True