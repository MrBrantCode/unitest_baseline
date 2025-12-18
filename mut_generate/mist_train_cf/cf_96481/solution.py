"""
QUESTION:
Implement a function `calculate_median(lst)` to find the median of a list of integers. The function should handle lists of any length, including those with duplicate elements and negative integers. The function should not use built-in sorting functions or libraries and should have a time complexity of O(nlogn) or better. If the input list is empty, return `None`. If the list has an odd length, return the middle element; if the list has an even length, return the average of the two middle elements.
"""

def calculate_median(lst):
    n = len(lst)
    if n == 0:
        return None
    sorted_lst = merge_sort(lst)
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        return (sorted_lst[(n // 2) - 1] + sorted_lst[n // 2]) / 2

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged