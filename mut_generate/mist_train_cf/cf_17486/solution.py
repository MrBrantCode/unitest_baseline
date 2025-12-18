"""
QUESTION:
Implement the `sort_by_absolute_value` function to sort a list of integers by their absolute value without using built-in sorting functions or methods. The function should have a time complexity of O(n^2) or better.
"""

def sort_by_absolute_value(lst):
    n = len(lst)
    
    for i in range(n):
        # Flag to check if any swaps are made in the current iteration
        swapped = False
        
        for j in range(0, n-i-1):
            if abs(lst[j]) > abs(lst[j+1]):
                # Swap the elements if the absolute value of the current element is greater than the next element
                lst[j], lst[j+1] = lst[j+1], lst[j]
                
                swapped = True
        
        # If no swaps were made in the current iteration, the list is already sorted
        if not swapped:
            break
    
    return lst