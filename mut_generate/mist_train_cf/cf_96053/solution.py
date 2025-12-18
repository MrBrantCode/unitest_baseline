"""
QUESTION:
Implement a function called `merge_sort_tuples` that sorts a list of tuples in ascending order by the first value of the tuple. The function should have a time complexity of O(n log n) or better and should be stable, meaning that tuples with the same first value maintain their relative order. The function should sort the list in place, without creating a new list or using any built-in sorting functions or libraries. The list can contain up to 1 million tuples, and each tuple can have up to 10 elements, with each element having up to 10 characters.
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