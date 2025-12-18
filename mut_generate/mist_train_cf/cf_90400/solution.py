"""
QUESTION:
Write a function named `merge_dictionaries` that takes in two dictionaries and returns a new dictionary. The returned dictionary should only contain keys that start with a vowel and have a value that is a multiple of 3, with values converted to strings and keys sorted in ascending order. If a key is present in both input dictionaries, the value in the second dictionary should overwrite the value in the first dictionary. The original input dictionaries should not be modified.
"""

def merge_dictionaries(dict1, dict2):
    vowels = ['a', 'e', 'i', 'o', 'u']
    merged_dict = {key: str(value) for key, value in (dict1 | dict2).items() if key[0].lower() in vowels and value % 3 == 0}
    return dict(sorted(merged_dict.items()))