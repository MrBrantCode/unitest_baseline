"""
QUESTION:
Develop a recursive function `find_first_and_last(lst, low, high, target)` that finds the first and last occurrence of a target value in a sorted list. The function should take a sorted list `lst`, the lowest index `low`, the highest index `high`, and the target value `target` as parameters, and return a tuple containing the indices of the first and last occurrence of the target value. Assume that the input list is sorted in ascending order. The function should not use Python's built-in `index()` function.
"""

def find_first_and_last(lst, low, high, target):
    if low > high:
        return -1, -1

    mid = low + (high - low) // 2
    if target == lst[mid]:
        first = mid if mid == 0 or target != lst[mid-1] else find_first_and_last(lst, low, mid-1, target)[0]
        last = mid if mid == len(lst)-1 or target != lst[mid+1] else find_first_and_last(lst, mid+1, high, target)[1]
        return (first, last)
        
    elif target < lst[mid]:
        return find_first_and_last(lst, low, mid-1, target)
    else:
        return find_first_and_last(lst, mid+1, high, target)