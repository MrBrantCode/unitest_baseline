"""
QUESTION:
Write a function `find_max_and_second_max` that takes a list of integers as input and returns a tuple containing the maximum and second maximum elements. The function should only iterate through the list once and should not use any built-in functions or libraries for finding the maximum element. If the list has less than two elements, the function should return `None`.
"""

def find_max_and_second_max(lst):
    if len(lst) < 2:
        return None

    max_val = lst[0]
    second_max_val = None

    for i in range(1, len(lst)):
        if lst[i] > max_val:
            second_max_val = max_val
            max_val = lst[i]
        elif second_max_val is None or lst[i] > second_max_val:
            second_max_val = lst[i]

    return max_val, second_max_val