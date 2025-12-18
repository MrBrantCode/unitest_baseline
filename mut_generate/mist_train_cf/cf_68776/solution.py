"""
QUESTION:
Implement a function `sort_dict_list(dict_list, attr_list, default_val)` that takes in a list of dictionaries `dict_list`, a list of attributes `attr_list` to sort by, and a default return value `default_val` when an attribute is not present in a dictionary. The function should return the sorted list of dictionaries based on the given attributes, handling non-existing attributes by assigning them a lower sort priority.
"""

def sort_dict_list(dict_list, attr_list, default_val=""):
    """
    Sort a list of dictionaries by multiple attributes. Non-existing attributes are handled
    and have a lower sort priority.

    Args:
      dict_list: List of dictionaries to be sorted
      attr_list: List of attributes to sort by
      default_val: Default return value when attribute is not present in a dictionary

    Returns:
      Sorted list of dictionaries
    """
    return sorted(dict_list, key=lambda d: tuple(d.get(attr, default_val) for attr in attr_list))