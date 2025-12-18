"""
QUESTION:
Write a function `merge_dicts` that takes three parameters: two dictionaries `dict1` and `dict2`, and a function `condition` that takes two arguments. The function should merge `dict1` and `dict2` into a new dictionary, giving precedence to the values in `dict1` if the `condition` is met. If a key is present only in `dict2`, it should be included in the merged dictionary. The function should return the merged dictionary.
"""

def merge_dicts(dict1, dict2, condition):
    """
    Merge two dictionaries, giving precedence to the values in dict1 if the condition is met.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.
        condition (function): A function that takes two arguments and returns a boolean.

    Returns:
        dict: The merged dictionary.
    """
    merged_dict = {k: (v if condition(v, dict2.get(k, v)) else dict2.get(k, v)) for k, v in dict1.items()}
    merged_dict.update({k: v for k, v in dict2.items() if k not in dict1})
    return merged_dict