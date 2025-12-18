"""
QUESTION:
Write a function `find_substrings` that takes two parameters: `string_list` and `sub_string`. The function should return a list of strings from `string_list` that contain `sub_string`, handling case insensitivity and overlapping occurrences. If `sub_string` is empty or null, the function should return 'Substring is empty or null!'. If no matches are found, the function should return 'No matches found.' The function should have a time complexity of O(n), where n is the total number of characters in `string_list`, and use a constant amount of extra space.
"""

def find_substrings(string_list, sub_string):
    # case when the substring is either empty or null
    if not sub_string:
        return 'Substring is empty or null!'
    
    # convert both the strings and the substring to lowercase to handle case insensitivity
    string_list = [i.lower() for i in string_list]
    sub_string = sub_string.lower()
    
    matched_strings = [i for i in string_list if sub_string in i]
    if not matched_strings:
        return 'No matches found.'
    return matched_strings