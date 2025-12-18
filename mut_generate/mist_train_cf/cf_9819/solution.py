"""
QUESTION:
Write a function `convert_list_to_dict(lst)` that takes a list of strings and returns a dictionary where each key is a unique string from the list (case-insensitive) and the corresponding value is a list of all strings from the list that match the key (case-sensitive). If there is only one matching string, the value is still a list with one element. The function should have a time complexity of O(n), where n is the length of the list, and a space complexity of O(m), where m is the number of unique keys in the list. The dictionary keys should be sorted in descending order.
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