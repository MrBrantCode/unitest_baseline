"""
QUESTION:
Write a function named `find_min` that finds the minimum value of a given list using a recursive algorithm, without using built-in functions or libraries. The function should take a list as a parameter and return the minimum value in the list. If the list is empty, the function should return `None`.
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