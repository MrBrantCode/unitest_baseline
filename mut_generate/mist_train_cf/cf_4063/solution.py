"""
QUESTION:
Create a recursive function named `find_max` that takes a list of numbers and its median as parameters. The function should return the maximum element in the list that is greater than the median. If no such element exists, the function should return `None`. The function must be implemented recursively. The input list and median are guaranteed to be valid.
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