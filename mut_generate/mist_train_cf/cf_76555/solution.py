"""
QUESTION:
Implement a function `sort_array` that takes an array of integers and non-integer values as input, separates the integers, sorts them in ascending order without using any built-in sort functions, and returns the sorted array of integers. The function should also handle non-integer values by identifying and excluding them from the sorting process.
"""

def sort_array(arr):
    int_arr = [val for val in arr if isinstance(val, int)]
    sorted_arr = []
    
    while int_arr:
        min_val = int_arr[0]  
        for val in int_arr: 
            if val < min_val:
                min_val = val 
        sorted_arr.append(min_val)
        int_arr.remove(min_val)

    return sorted_arr