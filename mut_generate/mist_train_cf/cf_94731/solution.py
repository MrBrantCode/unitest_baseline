"""
QUESTION:
Implement the `sort_by_absolute_value` function to sort a list of integers by their absolute value without using any built-in sorting functions or methods. The function should have a time complexity of O(n^2) or better.
"""

def sort_by_absolute_value(lst):
    n = len(lst)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if abs(lst[j]) > abs(lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                
                swapped = True
        
        if not swapped:
            break
    
    return lst