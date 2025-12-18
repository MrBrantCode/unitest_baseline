"""
QUESTION:
Create a function `find_max_and_index` that takes a list of integers as input and returns a tuple containing the maximum number and its index. The function must not use any built-in Python functions or libraries to search or sort. The list is guaranteed to contain at least one element.
"""

def find_max_and_index(lst):
    max_num = lst[0]
    max_index = 0
    for i in range(1, len(lst)):
        if lst[i] > max_num:
            max_num = lst[i]
            max_index = i
    return (max_num, max_index)