"""
QUESTION:
Write a function named `second_biggest` that takes a list of values as input and returns the second largest value in the list. The function should not use any built-in sorting functions.
"""

def second_biggest(lst):
    if len(lst) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in lst:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    return second_max