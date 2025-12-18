"""
QUESTION:
Write a function called `find_median` that takes a list of integers as input and returns the median of the values. The function should return `None` if the list is empty. The function should be able to handle negative integers and floating-point numbers in the list, and its time complexity should be O(nlogn), where n is the length of the input list.
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