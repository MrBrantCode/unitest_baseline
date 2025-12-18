"""
QUESTION:
Write a function named find_median that takes a list of integers as input, including negative integers and floating-point numbers, and returns the median of the values. If the list is empty, the function should return None. The function should have a time complexity of O(nlogn), where n is the length of the input list.
"""

def find_median(lst):
    if not lst:  
        return None
    
    sorted_lst = sorted(lst)  
    
    if len(sorted_lst) % 2 == 1:  
        return sorted_lst[len(sorted_lst) // 2]
    else:  
        mid1 = sorted_lst[len(sorted_lst) // 2]
        mid2 = sorted_lst[len(sorted_lst) // 2 - 1]
        return (mid1 + mid2) / 2