"""
QUESTION:
Implement a function `linear_search_last` that takes a list and a target value as input, and returns the index of the last occurrence of the target value in the list. The list can have a maximum length of 10^6 and the target value can be of any data type. If the target value is not found in the list, return -1.
"""

def linear_search_last(lst, target):
    index = -1
    for i in range(len(lst)):
        if lst[i] == target:
            index = i
    return index