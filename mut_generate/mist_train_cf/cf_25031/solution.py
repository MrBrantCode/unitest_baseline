"""
QUESTION:
Write a function `merge_sort` that sorts a large array of integers in ascending order using the merge sort algorithm, which has a time complexity of O(nlog(n)). The function should take one argument, a list of integers, and return a sorted list of integers. The input list can contain duplicate values and may not be sorted initially.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result