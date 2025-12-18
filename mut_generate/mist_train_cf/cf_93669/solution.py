"""
QUESTION:
Write a function `find_longest_common_prefix` to find the longest common prefix in the keys of dictionaries from a given array of dictionaries. The function should be case-sensitive, only consider alphabetic characters, and ignore non-alphabetic characters. If there is no common prefix, return an empty string. The function should handle large inputs (up to 10^6 dictionaries and keys, and 100 characters per key), run within a time limit of 1 second, and minimize memory usage (not exceeding 1GB).
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