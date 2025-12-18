"""
QUESTION:
Write a function named `find_min` that takes a list as input and returns the minimum value in the list using a recursive algorithm. Do not use any built-in functions or libraries. If the list is empty, return `None`.
"""

def find_min(lst):
    if not lst:  
        return None
    elif len(lst) == 1:  
        return lst[0]
    else:
        mid = len(lst) // 2
        min1 = find_min(lst[:mid])  
        min2 = find_min(lst[mid:])  
        return min(min1, min2)  