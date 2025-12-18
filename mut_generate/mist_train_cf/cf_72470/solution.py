"""
QUESTION:
Write a function named `common` that takes three lists `l1`, `l2`, and `l3` as input and returns a list of unique elements that exist in at least two of the three lists. The function should not use any built-in Python list functions for sorting and removing duplicates. It should implement custom sorting and duplicate removal functions to achieve the result. The returned list should be sorted in ascending order.
"""

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    
    return merge(left, right)

def merge(left, right):
    lst = []
    while left and right:
        if left[0] < right[0]: 
            lst.append(left.pop(0)) 
        else: 
            lst.append(right.pop(0)) 
    if left: 
        lst += left
    elif right: 
        lst += right
    return lst

def remove_duplicates(lst):
    unique_list = []
    last_element = None
    for element in lst:
        if element != last_element:
            unique_list.append(element)
            last_element = element
    return unique_list

def entrance(l1: list, l2: list, l3: list):
    common_elements = []
    for i in l1:
        if (i in l2 or i in l3) and i not in common_elements:
            common_elements.append(i)
    common_elements = merge_sort(common_elements)
    common_elements = remove_duplicates(common_elements)
    return common_elements