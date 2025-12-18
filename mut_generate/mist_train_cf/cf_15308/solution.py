"""
QUESTION:
Implement the function `sort_unique_descending(lst)` that sorts the input list `lst` of integers in descending order, removes any duplicate elements, and returns the resulting list. The function must use O(1) extra space and have a time complexity of O(n log n), where n is the length of the list.
"""

def sort_unique_descending(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left_sorted = sort_unique_descending(left)
    right_sorted = sort_unique_descending(right)

    sorted_lst = merge(left_sorted, right_sorted)
    unique_lst = remove_duplicates(sorted_lst)

    return unique_lst


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def remove_duplicates(lst):
    unique_lst = []

    last_seen = None
    for num in lst:
        if num != last_seen:
            unique_lst.append(num)
        last_seen = num

    return unique_lst