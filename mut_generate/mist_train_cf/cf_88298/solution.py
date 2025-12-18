"""
QUESTION:
Write a recursive function `find_max(lst, median)` that finds the maximum element in the given list `lst` while ensuring that the maximum element is greater than the median of all the elements in the list. The function should return `None` if no such element exists. The input list `lst` is not empty and contains at least one integer. The input `median` is a number representing the median of the elements in `lst`.
"""

def find_max(lst, median):
    if len(lst) == 1:
        if lst[0] > median:
            return lst[0]
        else:
            return None
    else:
        mid = len(lst) // 2
        left_max = find_max(lst[:mid], median)
        right_max = find_max(lst[mid:], median)
        
        if left_max is None:
            return right_max
        elif right_max is None:
            return left_max
        else:
            return max(left_max, right_max)