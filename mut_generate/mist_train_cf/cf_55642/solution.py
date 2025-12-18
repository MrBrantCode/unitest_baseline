"""
QUESTION:
Write a function `find_second_smallest_greatest` that takes a list of numbers as input and returns the second smallest and second greatest numbers. The input list may contain integers, floating-point numbers, and repeating numbers. The function should handle edge cases where the list contains fewer than 4 unique numbers, including the cases where there are less than 2 unique items. The function should return a message in these edge cases instead of the second smallest and second greatest numbers.
"""

def find_second_smallest_greatest(lst):
    unique_lst = list(set(lst))
    
    if len(unique_lst) < 4:
        if len(unique_lst) < 2:
            return 'List must contain at least 2 unique items.'
        else:
            return 'List must contain at least 4 unique items.'
    
    unique_lst.sort()

    return unique_lst[1], unique_lst[-2]