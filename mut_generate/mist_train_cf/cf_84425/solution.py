"""
QUESTION:
Write a function `sort_strings(lst)` that sorts the strings in a list of mixed variable types (integers, strings, and booleans) alphabetically while preserving the original order of non-string variables. The function should ignore integers and booleans, and only sort the strings in the list.
"""

def sort_strings(lst):
    # Separate strings and others
    strings = sorted([i for i in lst if type(i) == str])
    others = [i for i in lst if type(i) != str]

    # Combine strings and others preserving the original order of non-string variables
    result = []
    ctr = 0
    for i in lst:
        if type(i) == str:
            result.append(strings[ctr])
            ctr += 1
        else:
            result.append(others.pop(0))
    return result