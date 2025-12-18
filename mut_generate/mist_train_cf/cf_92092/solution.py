"""
QUESTION:
Implement a function `format_list` that takes a list of strings and returns the list sorted in descending order of the number of characters in each string. The time complexity of the function should be O(nlogn), where n is the number of strings in the list. No built-in sorting functions are allowed. If two strings have the same number of characters, their original order should be preserved.
"""

def format_list(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = format_list(lst[:mid])
    right = format_list(lst[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if len(left[i]) >= len(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged