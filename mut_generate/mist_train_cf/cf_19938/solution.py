"""
QUESTION:
Implement the `find_max` function to find the maximum value in an array of integers while tracking the number of comparisons made. The function should take an array as input and return the maximum value and the total number of comparisons. The function must be implemented recursively without using any loops. The array can be empty, and the function should handle this case accordingly.
"""

def find_max(arr):
    if len(arr) == 0:  
        return None, 0
    
    if len(arr) == 1:  
        return arr[0], 0
    
    mid = len(arr) // 2  
    
    left_max, left_comp = find_max(arr[:mid])
    right_max, right_comp = find_max(arr[mid:])
    
    if left_max > right_max:
        return left_max, left_comp + right_comp + 1
    else:
        return right_max, left_comp + right_comp + 1