"""
QUESTION:
Create a function `find_second_max_min` that takes a list of integers and returns a tuple containing the second highest and second lowest values of the list. The function should return `None` if the list is empty or contains less than three elements. If the list contains only three elements, the function should return a tuple with the second highest and second lowest values as the same element.
"""

def find_second_max_min(lst):
    if len(lst) < 3:
        return None
    elif len(lst) == 3:
        return (lst[1], lst[1])
    else:
        max_val = float('-inf')
        second_max_val = float('-inf')
        min_val = float('inf')
        second_min_val = float('inf')
        for num in lst:
            if num > max_val:
                second_max_val = max_val
                max_val = num
            elif num > second_max_val and num != max_val:
                second_max_val = num
            if num < min_val:
                second_min_val = min_val
                min_val = num
            elif num < second_min_val and num != min_val:
                second_min_val = num
        return (second_max_val, second_min_val)