"""
QUESTION:
Write a function called `merge_dictionaries` that takes two dictionaries `dict1` and `dict2` as input, merges them into a new dictionary, and returns the merged dictionary. The merged dictionary should only contain keys that start with a vowel and have a value that is a multiple of 3. The keys in the merged dictionary should be sorted in ascending order, and the values should be converted to strings. If a key is present in both `dict1` and `dict2`, the value from `dict2` should overwrite the value from `dict1`. The original dictionaries `dict1` and `dict2` should not be modified.
"""

def merge_dictionaries(dict1, dict2):
    vowels = ['a', 'e', 'i', 'o', 'u']
    merged_dict = {}

    for key in dict1.keys():
        if key[0].lower() in vowels and dict1[key] % 3 == 0:
            merged_dict[key] = str(dict1[key])

    for key in dict2.keys():
        if key[0].lower() in vowels and dict2[key] % 3 == 0:
            merged_dict[key] = str(dict2[key])

    return dict(sorted(merged_dict.items()))