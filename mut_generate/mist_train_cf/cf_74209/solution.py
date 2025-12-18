"""
QUESTION:
Implement a function called `common` that takes two lists `l1` and `l2` as input, and returns a list of unique common elements between `l1` and `l2`, sorted in ascending order. The function should not use any built-in Python list functions or set operations. Instead, implement custom functions for sorting and duplicate removal.
"""

def bubble_sort(lst: list):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def unique(lst: list):
    unique_list = []
    for elem in lst:
        if elem not in unique_list:
            unique_list.append(elem)
    return unique_list
    
def common_elements(l1: list, l2: list):
    common_elements = []
    for i in l1:
        if i in l2 and i not in common_elements:
            common_elements.append(i)            
    return bubble_sort(unique(common_elements))