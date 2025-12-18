"""
QUESTION:
Write a function `merge_and_sort_dicts` that takes two dictionaries as input and returns a new dictionary. The new dictionary should contain all key-value pairs from both input dictionaries. If there are matching keys, the values from the second dictionary should be prioritized. The resulting dictionary should be sorted in ascending order of its keys.
"""

def merge_and_sort_dicts(dict1, dict2):
    """
    Merge two dictionaries into one, prioritizing values from the second dictionary
    and return the result sorted by keys in ascending order.

    Args:
        dict1 (dict): The first dictionary to merge.
        dict2 (dict): The second dictionary to merge.

    Returns:
        dict: A new dictionary containing all key-value pairs from both input dictionaries,
              sorted by keys in ascending order.
    """
    # Use the dict.update() method to merge dict2 into dict1
    # If a key exists in both, the value from dict2 will overwrite the one in dict1
    merged_dict = dict1.copy()  # Create a copy to avoid modifying the original dict
    merged_dict.update(dict2)

    # Use the sorted() function and dict comprehension to create a new dictionary that's sorted by keys
    sorted_dict = {k: merged_dict[k] for k in sorted(merged_dict)}

    return sorted_dict