"""
QUESTION:
Write a function `find_max_value` that takes a list of integers as input and returns the maximum value in the list. The function should not use any built-in functions or libraries and should have a time complexity of O(n), where n is the number of elements in the list. If the list contains duplicate maximum values, the function should return the first occurrence of the maximum value. If the list is empty, the function should return None.
"""

def find_max_value(lst):
    if not lst:  
        return None
    
    max_value = lst[0]  
    
    for num in lst:
        if num > max_value:  
            max_value = num
    
    return max_value