"""
QUESTION:
Create a function called `merge_dicts` that takes two dictionaries `dictA` and `dictB` as input. The function should merge these dictionaries into one, excluding any keys that start with a vowel (either lowercase or uppercase). The resulting dictionary should be sorted in descending order based on the values of the keys.
"""

def merge_dicts(dictA, dictB):
    """
    Merge two dictionaries into one, excluding any keys that start with a vowel (either lowercase or uppercase).
    The resulting dictionary is sorted in descending order based on the values of the keys.

    Args:
        dictA (dict): The first dictionary to be merged.
        dictB (dict): The second dictionary to be merged.

    Returns:
        dict: The merged dictionary.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    merged_dict = {}

    for key, value in dictA.items():
        if key[0].lower() not in vowels:
            merged_dict[key] = value

    for key, value in dictB.items():
        if key[0].lower() not in vowels:
            merged_dict[key] = value

    merged_dict = dict(sorted(merged_dict.items(), key=lambda x: x[1], reverse=True))
    return merged_dict