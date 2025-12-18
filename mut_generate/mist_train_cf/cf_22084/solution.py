"""
QUESTION:
Write a function `sum_of_lists` that takes in a list of lists as a parameter. The input list of lists contains elements that can be integers, floating-point numbers, or nested lists with varying depths. The function should return the sum of all the elements in the input lists. The function should handle empty lists by returning 0, skip nested empty lists, and correctly handle negative integers and floating-point numbers.
"""

def sum_of_lists(lists):
    total_sum = 0
    
    for sublist in lists:
        if isinstance(sublist, list) and sublist:
            total_sum += sum_of_lists(sublist)
        elif isinstance(sublist, (int, float)):
            total_sum += sublist
    
    return total_sum