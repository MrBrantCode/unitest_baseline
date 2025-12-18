"""
QUESTION:
Write a function `find_max_value` that takes a list of integers as input and returns the maximum value in the list. The function should not use any built-in functions or libraries to find the maximum value, and its time complexity should be O(n), where n is the number of elements in the list.
"""

def find_max_value(lst):
    max_val = lst[0]  
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val