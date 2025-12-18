"""
QUESTION:
Implement a function called `find_target_index` that takes a list of integers and a target integer as input. The function should return the index of the last occurrence of the target integer in the list. If the target integer is not present, return -1.
"""

def find_target_index(lst, target):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == target:
            return i
    return -1