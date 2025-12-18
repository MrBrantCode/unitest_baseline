"""
QUESTION:
Create a function `filter_strings` that takes a list of strings and/or nested lists of strings, and an integer `n`, as input. The function should return a combined list of strings with all strings converted to lower case, filtered to only include strings with `n` or fewer characters. The function should handle nested lists by calling itself recursively.
"""

def filter_strings(lst, n):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(filter_strings(item, n))  # recursive call for nested lists
        elif isinstance(item, str) and len(item) <= n:
            result.append(item.lower())
    return result