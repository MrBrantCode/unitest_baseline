"""
QUESTION:
Write a function `second_biggest(lst)` that takes a list of numbers as input and returns the second largest number in the list. The function must not use any built-in sorting functions.
"""

def second_biggest(lst):
    if len(lst) < 2:
        return None
    
    max_num = second_max = float('-inf')
    
    for num in lst:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num < max_num:
            second_max = num
            
    if second_max == float('-inf'):
        return None
    
    return second_max