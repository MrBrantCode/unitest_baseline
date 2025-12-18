"""
QUESTION:
Write a function `group_strings` that takes a list of strings as input. The function should return a dictionary where the keys are the first two characters of each string and the values are lists of strings that start with those characters. The function should handle duplicate strings by removing them and sort the values in alphabetical order.
"""

def group_strings(strings):
    string_dict = {}
    for string in strings:
        key = string[:2]
        if key not in string_dict:
            string_dict[key] = []
        string_dict[key].append(string)
    for key in string_dict:
        string_dict[key] = sorted(list(set(string_dict[key])))
    return string_dict