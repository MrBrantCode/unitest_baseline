"""
QUESTION:
Create a function named `reverse_sort_dict` that takes a dictionary as an argument and returns a new dictionary. The new dictionary should be created by reversing the original dictionary, then sorting its items by the length of the values in descending order, and finally sorting its keys in ascending order based on their corresponding values in the original dictionary.
"""

def reverse_sort_dict(dictionary):
    reversed_dict = dict(reversed(dictionary.items()))
    sorted_dict = {k: v for k, v in sorted(reversed_dict.items(), key=lambda item: len(item[1]), reverse=True)}
    sorted_keys = sorted(sorted_dict.keys(), key=lambda k: dictionary[k])
    sorted_dict = {k: sorted_dict[k] for k in sorted_keys}
    return sorted_dict