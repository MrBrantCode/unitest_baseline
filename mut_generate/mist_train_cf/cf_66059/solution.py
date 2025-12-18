"""
QUESTION:
Write a recursive function `merge_sort` to sort an array of strings alphabetically in a case-insensitive manner. The array may contain non-alphabetical characters such as numbers, symbols, and spaces. The function should return the sorted array.
"""

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_list = merge_sort(lst[:mid])
    right_list = merge_sort(lst[mid:])

    return merge(left_list, right_list)

def merge(left_list, right_list):
    merged = []
    while left_list and right_list:
        if left_list[0].lower() < right_list[0].lower():
            merged.append(left_list.pop(0))
        else:
            merged.append(right_list.pop(0))

    # In case one of the lists is not empty
    merged.extend(left_list if left_list else right_list)

    return merged