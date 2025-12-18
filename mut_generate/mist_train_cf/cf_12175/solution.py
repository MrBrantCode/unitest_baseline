"""
QUESTION:
Write a function `find_max_min_second_max_second_min` that takes a list of integers as input and returns the maximum value, minimum value, second maximum value, and second minimum value. The function should handle duplicate values by not considering the same value as both the maximum/minimum and second maximum/minimum.
"""

def find_max_min_second_max_second_min(lst):
    max_value = float('-inf')
    second_max_value = float('-inf')
    min_value = float('inf')
    second_min_value = float('inf')

    for num in lst:
        if num > max_value:
            second_max_value = max_value
            max_value = num
        elif num > second_max_value and num != max_value:
            second_max_value = num
        
        if num < min_value:
            second_min_value = min_value
            min_value = num
        elif num < second_min_value and num != min_value:
            second_min_value = num
    
    return max_value, min_value, second_max_value, second_min_value