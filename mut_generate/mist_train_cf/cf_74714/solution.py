"""
QUESTION:
Write a function `get_longest_str_of_all_lists` that takes a list of lists of strings as input. The function should find the longest string in each non-empty sub-list, compare these longest strings, and return the length of the longest string. If multiple strings have the same maximum length, any of them can be considered. The function should handle null or empty sub-lists.
"""

def get_longest_str_of_all_lists(list_of_lists):
    max_len = 0
    for sublist in list_of_lists:
        if sublist:
            longest_str_in_sublist = max(sublist, key=len)
            if len(longest_str_in_sublist) > max_len:
                max_len = len(longest_str_in_sublist)
    return max_len