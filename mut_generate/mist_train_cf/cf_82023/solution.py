"""
QUESTION:
Implement a function `filter_strings` that filters a list of strings based on multiple search conditions. The function should take a list of strings and three optional parameters: `keyword` for keyword search, `case_sensitive` (default is `False`) for case sensitivity option, and `pattern` for regular expressions using the `re` module. The function should return a list of strings that meet the specified criteria.
"""

import re

def filter_strings(lst, keyword=None, case_sensitive=False, pattern=None):
    filtered_lst = []
    for string in lst:
        if keyword:
            if case_sensitive:
                if keyword in string:
                    filtered_lst.append(string)
            else:
                if keyword.lower() in string.lower():
                    filtered_lst.append(string)
        elif pattern:
            if re.search(pattern, string):
                filtered_lst.append(string)
    return filtered_lst