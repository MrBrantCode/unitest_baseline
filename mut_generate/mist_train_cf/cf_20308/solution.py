"""
QUESTION:
Create a function `merge_sort_tuples` that takes a list of tuples as input, where each tuple can have up to 10 elements and each element can have up to 10 characters. The list can contain up to 1 million tuples. The function should sort the list in ascending order based on the first value of each tuple, maintain the relative order of tuples with the same first value, and have a time complexity of O(n log n) or better. The sorting should be performed in place, without creating a new list or using any built-in sorting functions or libraries.
"""

def merge_sort_tuples(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    left_half = merge_sort_tuples(left_half)
    right_half = merge_sort_tuples(right_half)

    return merge_tuples(left_half, right_half)


def merge_tuples(left_half, right_half):
    merged = []
    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i][0] <= right_half[j][0]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    while i < len(left_half):
        merged.append(left_half[i])
        i += 1

    while j < len(right_half):
        merged.append(right_half[j])
        j += 1

    return merged