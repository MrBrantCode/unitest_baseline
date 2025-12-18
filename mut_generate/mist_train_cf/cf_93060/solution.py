"""
QUESTION:
Write a function `find_second_largest(arr)` that takes a list of integers as input and returns the second largest element in the list. If the list has less than two distinct elements, the function should return the smallest possible integer value (`float('-inf')`). Assume that the input list does not contain duplicate maximum values.
"""

def find_second_largest(arr):
    max_num = float('-inf')
    second_max_num = float('-inf')
    
    for num in arr:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    
    return second_max_num