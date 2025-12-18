"""
QUESTION:
Implement a `sort_list` function in a class that sorts a list of numbers in ascending order using a divide and conquer strategy with a time complexity of O(nlogn).
"""

def sort_list(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    left = sort_list(left)
    right = sort_list(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result