"""
QUESTION:
Create a function `find_second_highest_number` that takes a list of integers as input and returns the second highest unique number. If the list has less than two elements, the function should return `None`. If the second highest number is not unique (i.e., there are multiple occurrences of the second highest number), the function should return the third highest unique number instead.
"""

def find_second_highest_number(lst):
    if len(lst) < 2:
        return None

    sorted_lst = sorted(set(lst), reverse=True)
    
    if len(sorted_lst) < 2:
        return None

    return sorted_lst[1]