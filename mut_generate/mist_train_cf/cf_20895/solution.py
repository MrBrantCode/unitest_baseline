"""
QUESTION:
Write a recursive function called `find_max_min` that finds the maximum and minimum elements in a list of integers. The function should follow these rules: 
- If the list is empty, return None.
- If the list contains only one element, return that element as both the maximum and minimum.
- Divide the list into two halves.
- Recursively find the maximum and minimum elements in each half.
- Return the larger of the two maximum elements and the smaller of the two minimum elements. 
Do not use built-in functions like max() or min() to find the maximum and minimum elements.
"""

def find_max_min(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0], lst[0]
    mid = len(lst) // 2
    left_max, left_min = find_max_min(lst[:mid])
    right_max, right_min = find_max_min(lst[mid:])
    return max(left_max, right_max), min(left_min, right_min)