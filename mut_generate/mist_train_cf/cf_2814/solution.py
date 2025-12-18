"""
QUESTION:
Write a function `move_second_to_beginning(lst)` that moves the second-to-last element of a given list to the beginning of the list without using built-in list manipulation methods or slicing operations. The function should have a time complexity of O(n), where n is the length of the list, and it should handle cases where the list has fewer than 2 elements by returning the original list.
"""

def move_second_to_beginning(lst):
    if len(lst) < 2:
        return lst
    
    second_last = lst[-2]
    for i in range(len(lst)-2, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = second_last
    
    return lst