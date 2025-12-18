"""
QUESTION:
Implement a function `merge_sort(lst)` that takes an integer list `lst` as input and returns a sorted list. The function should have a time complexity of O(n log n) and a space complexity of O(1). The function should be stable, preserving the relative order of elements with equal values, and handle duplicate elements in the input list.
"""

def merge_sort(lst):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)