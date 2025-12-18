"""
QUESTION:
Design a function `filter_lst` that takes a list `lst` and an integer `n` as input, and returns a list of numbers that are greater than or equal to `n`. The function should handle nested lists by recursively invoking itself on the nested list and combining the results.
"""

def filter_lst(lst, n):
    result = []
    for item in lst:
        if type(item) == list:
            result.extend(filter_lst(item, n))
        elif item >= n:
            result.append(item)
    return result