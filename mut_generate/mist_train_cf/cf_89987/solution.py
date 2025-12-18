"""
QUESTION:
Write a function called `sum_of_lists` that takes a list of lists as a parameter and returns the sum of all the elements in the input lists. The input list of lists can contain integers and/or floats, and can be nested to varying depths. The function should handle empty lists, nested empty lists, and negative integers. If the input list of lists is empty, the function should return 0.
"""

def sum_of_lists(lists):
    total_sum = 0
    
    for lst in lists:
        if isinstance(lst, list):
            total_sum += sum_of_lists(lst)
        else:
            total_sum += lst
    
    return total_sum