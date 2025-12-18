"""
QUESTION:
Write a function called `convert_list_to_dict` that takes a list of strings as input and returns a dictionary. The function should handle duplicate keys in the list by combining their corresponding values into a list. The function should be case-insensitive when comparing keys and sort the dictionary keys in descending order. The function should have a time complexity of O(n), where n is the length of the list, and a space complexity of O(m), where m is the number of unique keys in the list.
"""

def convert_list_to_dict(lst):
    dict = {}
    for string in lst:
        key = string.lower()
        if key in dict:
            dict[key].append(string)
        else:
            dict[key] = [string]

    sorted_keys = sorted(dict.keys(), reverse=True)
    sorted_dict = {key: dict[key] for key in sorted_keys}
    return sorted_dict