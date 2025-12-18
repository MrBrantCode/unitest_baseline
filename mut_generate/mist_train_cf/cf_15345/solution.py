"""
QUESTION:
Write a function `find_longest_common_prefix` that finds the longest common prefix among all keys of dictionaries in a given array of dictionaries. The prefix should be case-sensitive and consist only of alphabetic characters. If there's no common prefix, return an empty string. The function should be efficient, handle large inputs (up to 10^6 dictionaries with up to 10^6 keys each, and keys up to 100 characters long), run within a 1-second time limit, and not exceed 1GB of memory usage. The function should also handle keys with special characters, spaces, punctuation marks, and numbers.
"""

def find_longest_common_prefix(arr_of_dictionaries):
    if not arr_of_dictionaries:
        return ""

    common_prefix = ""
    first_dict = arr_of_dictionaries[0]

    for key in first_dict.keys():
        if key.isalpha():
            for dict in arr_of_dictionaries[1:]:
                if key not in dict or dict[key] != first_dict[key]:
                    return common_prefix
            common_prefix += key

    return common_prefix