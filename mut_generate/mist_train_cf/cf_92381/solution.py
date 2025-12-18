"""
QUESTION:
Write a function `last_occurrence_index` that takes two parameters: `lst` (the list to search) and `value` (the value to find the last occurrence of). The function should return the index of the value if it is present in the list, and if it appears more than once, return the index of the last occurrence. If the value is not present, return -1.
"""

def last_occurrence_index(lst, value):
    if value not in lst:
        return -1
    else:
        return len(lst) - lst[::-1].index(value) - 1