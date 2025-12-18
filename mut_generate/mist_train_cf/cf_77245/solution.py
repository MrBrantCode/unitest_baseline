"""
QUESTION:
Implement a function `get_max(lst)` that calculates the maximum element in a given list without using any built-in functions or libraries. The function should handle large datasets effectively. It should return `None` if the input list is empty.
"""

def get_max(lst):
    if len(lst) == 0:
        return None
    max_number = lst[0]
    for num in lst:
        if num > max_number:
            max_number = num
    return max_number