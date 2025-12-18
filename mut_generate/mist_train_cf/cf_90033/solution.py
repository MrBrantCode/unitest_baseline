"""
QUESTION:
Write a function `weighted_average` that calculates the weighted average of numbers in a list, where each number is multiplied by its index position and divided by the sum of index positions. The function should handle cases with non-integer values, negative numbers, and nested lists, and return the weighted average rounded to 2 decimal places. If the sum of index positions is 0, return 0. The function should have a time complexity of O(n), where n is the total number of elements in the input list.
"""

def weighted_average(lst):
    flattened_lst = [item for sublist in lst for item in sublist] if any(isinstance(item, list) for item in lst) else lst
    index_sum = sum(range(len(flattened_lst)))
    
    if index_sum == 0:
        return 0
    
    weighted_sum = sum(i * num for i, num in enumerate(flattened_lst))
    weighted_average = weighted_sum / index_sum
    
    return round(weighted_average, 2)