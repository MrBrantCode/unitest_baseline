"""
QUESTION:
Write a function named `find_max_value` that takes a list of integers as input and returns the maximum value in the list without using any built-in functions or libraries. The function should have a time complexity of O(n), where n is the number of elements in the list.
"""

def entance(lst):
    max_val = lst[0]  
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val