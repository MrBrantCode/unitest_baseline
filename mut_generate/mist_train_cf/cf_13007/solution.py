"""
QUESTION:
Implement a function called `delete_last_occurrence` that takes a list `lst` and a value as input, and returns the modified list with the last occurrence of the specified value deleted. The function should not use any built-in list methods or functions for deletion, and should only modify the list if the specified value is found. The input list can contain up to 10^6 elements and may contain duplicate values.
"""

def delete_last_occurrence(lst, value):
    last_index = -1
    
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == value:
            last_index = i
            break
    
    if last_index == -1:
        return lst
    
    return lst[:last_index] + lst[last_index+1:]