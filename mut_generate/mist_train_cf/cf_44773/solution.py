"""
QUESTION:
Write a function named `second_largest` that takes a list as input and returns the second largest element along with its index in the original list. The function should handle the case when there are duplicate elements in the list and should not use any built-in functions to find the largest element.
"""

def entrance(lst):
    max_num = float('-inf')
    sec_max = float('-inf')
    max_index = -1
    sec_max_index = -1
    
    for i, number in enumerate(lst):
        if number > max_num:
            sec_max = max_num
            sec_max_index = max_index
            max_num = number
            max_index = i
        elif number < max_num and number > sec_max:
            sec_max = number
            sec_max_index = i
            
    return sec_max, sec_max_index