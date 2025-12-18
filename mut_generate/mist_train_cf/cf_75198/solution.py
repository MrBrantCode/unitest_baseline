"""
QUESTION:
Write a function `find_nearest(numbers_list, target)` that finds all integers in `numbers_list` closest to `target`. The function should return a list of integers with the smallest absolute difference to `target`, handling multiple occurrences and outliers.
"""

def find_nearest(numbers_list, target):
    smallest_diff = float('inf')  
    nearest_values = []  
    for num in numbers_list:
        diff = abs(target - num)
        if diff < smallest_diff:  
            smallest_diff = diff   
            nearest_values = [num]  
        elif diff == smallest_diff:  
            nearest_values.append(num)  
    return nearest_values