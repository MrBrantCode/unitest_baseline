"""
QUESTION:
Write a function `group_Strings(lst)` that groups a list of strings based on the frequency of alphanumeric characters used in them. The function should be case-insensitive and ignore non-alphanumeric characters and spaces.
"""

from collections import Counter

def group_Strings(lst):
    temp_dict = {}

    for string in lst:
        key = tuple(sorted(Counter(filter(str.isalnum, string.lower())).items()))
        if key in temp_dict:
            temp_dict[key].append(string)
        else:
            temp_dict[key] = [string]
    return list(temp_dict.values())