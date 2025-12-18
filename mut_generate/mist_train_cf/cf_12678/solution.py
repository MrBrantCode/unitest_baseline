"""
QUESTION:
Write a function `find_maximum` that takes a list of numbers as input and returns the maximum element in the list. The function should not use any built-in functions for finding the maximum value, and it should be able to handle lists containing duplicate elements.
"""

def find_maximum(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num