"""
QUESTION:
Create a function `append_odd_lists(list_1, list_2)` that appends elements from `list_2` to `list_1`, but only if both lists have the same length and the elements being appended from `list_2` and the corresponding elements in `list_1` are odd numbers. The function should have a time complexity of O(n), where n is the length of the lists, and a space complexity of O(n), where n is the number of appended elements. If the lists have different lengths, return an empty list.
"""

def append_odd_lists(list_1, list_2):
    if len(list_1) == len(list_2):
        return [x for i, x in enumerate(list_1) for y in [list_2[i]] if x % 2 != 0 and y % 2 != 0]
    else:
        return []