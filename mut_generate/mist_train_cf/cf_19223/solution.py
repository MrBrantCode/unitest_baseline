"""
QUESTION:
Implement a function named `update_array` that takes an array of integers as input. Replace all the zeroes in the array with the nearest non-zero element on the left side of the zero. If there is no non-zero element on the left side, replace the zero with the nearest non-zero element on the right side. If there are no non-zero elements on either side, replace the zero with -1.
"""

def update_array(arr):
    n = len(arr)
    left_non_zero = -1
    right_non_zero = -1
    
    for i in range(n):
        if arr[i] != 0:
            left_non_zero = arr[i]
        elif left_non_zero != -1:
            arr[i] = left_non_zero
        elif right_non_zero != -1:
            arr[i] = right_non_zero
        else:
            arr[i] = -1
        
        if arr[i] != 0:
            right_non_zero = arr[i]
    
    return arr