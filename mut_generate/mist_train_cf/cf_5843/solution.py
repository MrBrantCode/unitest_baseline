"""
QUESTION:
Create a function `merge_objects` that takes two parameters, `a` and `b`, and merges them into a single object. The function should not use built-in merge functions or methods. The merged object should have all keys from both input objects, with the second object overwriting the first object in case of duplicate keys. The merged object should be sorted in descending order based on keys. Only keys containing alphabetic characters (A-Z, a-z) should be included in the merged object, excluding any keys with non-alphabetic characters. The function should handle nested objects within the input objects and merge them accordingly.
"""

def merge_objects(a, b):
    """
    Merge two objects into a single object.

    The function merges two input objects into a single object. The merged object
    has all keys from both input objects, with the second object overwriting the
    first object in case of duplicate keys. The merged object is sorted in
    descending order based on keys. Only keys containing alphabetic characters
    (A-Z, a-z) are included in the merged object, excluding any keys with
    non-alphabetic characters. The function handles nested objects within the
    input objects and merges them accordingly.

    Parameters:
    a (dict): The first object to merge.
    b (dict): The second object to merge.

    Returns:
    dict: The merged object.
    """

    def merge_nested(merged, key, nested):
        """
        Recursively merge nested objects.

        Parameters:
        merged (dict): The merged object.
        key (str): The key of the nested object.
        nested (dict): The nested object to merge.
        """
        if key not in merged:
            merged[key] = {}
        for nested_key, nested_value in nested.items():
            if isinstance(nested_value, dict):
                merge_nested(merged[key], nested_key, nested_value)
            elif nested_key.isalpha():
                merged[key][nested_key] = nested_value

    merged = {}

    # Merge the first object into the merged object
    for key, value in a.items():
        if isinstance(value, dict):
            merge_nested(merged, key, value)
        elif key.isalpha():
            merged[key] = value

    # Merge the second object into the merged object
    for key, value in b.items():
        if isinstance(value, dict):
            merge_nested(merged, key, value)
        elif key.isalpha():
            merged[key] = value

    # Sort the merged object in descending order based on keys
    return dict(sorted(merged.items(), key=lambda item: item[0], reverse=True))