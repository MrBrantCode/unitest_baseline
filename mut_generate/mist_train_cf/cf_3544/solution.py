"""
QUESTION:
Write a function `merge_and_sort_dicts` that takes two dictionaries `dictA` and `dictB` as input, merges them into a single dictionary, and returns the merged dictionary sorted in descending order based on the values of the keys. The merged dictionary should exclude any keys that start with a vowel. If two keys have the same value, they should be sorted alphabetically. If there are duplicate values, remove them from the merged dictionary.
"""

def merge_and_sort_dicts(dictA, dictB):
    """
    Merges two dictionaries, excludes keys starting with a vowel, 
    sorts the merged dictionary in descending order based on values and keys, 
    and removes duplicate values.

    Args:
        dictA (dict): The first dictionary.
        dictB (dict): The second dictionary.

    Returns:
        dict: The merged dictionary.
    """
    merged_dict = {}

    # Merge dictionaries while excluding keys starting with a vowel
    for key, value in dictA.items():
        if key[0].lower() not in ['a', 'e', 'i', 'o', 'u']:
            merged_dict[key] = value

    for key, value in dictB.items():
        if key[0].lower() not in ['a', 'e', 'i', 'o', 'u']:
            merged_dict[key] = value

    # Sort the merged dictionary in descending order based on values and keys
    merged_dict = dict(sorted(merged_dict.items(), key=lambda x: (-x[1], x[0])))

    # Remove duplicate values from the merged dictionary
    merged_dict = {key: value for key, value in merged_dict.items() if list(merged_dict.values()).count(value) == 1}

    return merged_dict