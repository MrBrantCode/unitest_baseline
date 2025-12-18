"""
QUESTION:
Write a function `find_all_occurrences(num, lst)` to find the positions of all occurrences of a specified integer `num` within a list `lst`. The function should return a list of indices where the specified integer is found. If the specified integer is not found in the list, the function should return an empty list.
"""

def find_all_occurrences(num, lst):
    indices = []
    for i in range(len(lst)):
        if lst[i] == num:
            indices.append(i)
    return indices