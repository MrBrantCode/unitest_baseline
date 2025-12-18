"""
QUESTION:
Write a function `find_maximum` that takes a list of integers as input and returns the maximum element from the list. The function should not use any built-in functions or libraries for finding the maximum element. The input list can be empty and can contain both positive and negative integers, including duplicate values. The function should have a time complexity of O(n), where n is the length of the list. If the input list is empty, the function should return `None`.
"""

def find_maximum(lst):
    if len(lst) == 0:
        return None
    
    max_num = lst[0]
    for num in lst[1:]:
        if num > max_num:
            max_num = num
    
    return max_num