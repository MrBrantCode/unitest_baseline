"""
QUESTION:
Implement a function named `delete_last_occurrence` that takes two parameters: a list `lst` and a value. The function should delete the last occurrence of the specified value from the list without using any built-in list methods or functions, and return the modified list. If the value is not found in the list, the function should return the original list. The input list can contain duplicates and may have up to 10^6 elements.
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