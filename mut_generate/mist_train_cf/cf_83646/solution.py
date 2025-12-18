"""
QUESTION:
Write a function named `move_zeros_to_end` that takes a list as input and moves all occurrences of the integer zero to the end of the list while maintaining the order of non-zero elements. The function should also handle nested lists within the input list and shift zeros to the end of these nested lists. The function must not use any pre-existing Python functions or libraries to directly solve the problem.
"""

def move_zeros_to_end(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            move_zeros_to_end(lst[i])
        else:
            count_zero = lst.count(0)
            lst[:] = [value for value in lst if value != 0]
            lst.extend([0]*count_zero)
    return lst