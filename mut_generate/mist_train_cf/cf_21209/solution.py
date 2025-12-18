"""
QUESTION:
Implement a function called `calculate_median` that calculates the median of a list of numbers. The function should be able to handle lists of any length, including lists with duplicate elements and negative numbers. The function should not use any built-in sorting functions or libraries. The time complexity of the function should be O(nlogn) or better.
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