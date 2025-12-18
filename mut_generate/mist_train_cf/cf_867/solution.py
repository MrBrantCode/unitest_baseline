"""
QUESTION:
Write a function `group_strings(strings)` that groups a list of strings based on the first two characters of each string and returns a dictionary where the keys are the first two characters and the values are lists of unique strings that start with those characters in alphabetical order.
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