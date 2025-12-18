"""
QUESTION:
Write a function `find_occurrences` that takes a list of integers `lst` and an integer `target` as input. The function should return a tuple containing the indices of the first and last occurrences of `target` in `lst`, and the count of occurrences of `target` in `lst`. If `target` does not exist in `lst`, the function should return -1. The function should not use built-in functions like `index()`, `count()`, or `in`.
"""

def find_occurrences(lst, target):
    first_index = -1
    last_index = -1
    count = 0
    
    for i in range(len(lst)):
        if lst[i] == target:
            if first_index == -1:  
                first_index = i
            last_index = i  
            count += 1  
    
    if first_index == -1:  
        return -1
    else:
        return (first_index, last_index, count)