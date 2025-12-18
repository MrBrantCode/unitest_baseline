"""
QUESTION:
Write a function `replace_duplicates_with_max` that takes a list of integers as input. The function should remove duplicates from the list while preserving the original order, and replace each removed duplicate with the maximum value from the list. The function should return the modified list. The input list is not empty and contains at least one integer.
"""

def replace_duplicates_with_max(lst):
    max_val = max(lst)
    seen = set()
    for i in range(len(lst)):
        if lst[i] in seen:
            lst[i] = max_val
        else:
            seen.add(lst[i])
    return lst