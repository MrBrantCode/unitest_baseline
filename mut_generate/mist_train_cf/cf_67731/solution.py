"""
QUESTION:
Develop a function `final_occurrence(array, target)` that takes a sorted array and a target element as input. The function should return the index of the last occurrence of the target element in the array. If the target element does not exist, return the message "The element does not exist in the array". The function should achieve a time complexity of better than O(n).
"""

def final_occurrence(array, target):
    lower, upper = 0, len(array)

    while lower < upper:
        mid = lower + (upper - lower) // 2
        if array[mid] <= target:
            lower = mid + 1
        else:
            upper = mid

    if lower-1 >= 0 and array[lower-1] == target:
        return lower - 1
    else:
        return "The element does not exist in the array"