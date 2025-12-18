"""
QUESTION:
Write a function named `shortest_increasing_subarray` that takes a list of integers and an optional argument specifying the minimum length of the subarray. The function should return the shortest continuous increasing subarray in the list that is above or equal to the specified minimum length. The minimum length of the subarray must be at least 2. The function should not use any external libraries or built-in sort function.
"""

def shortest_increasing_subarray(arr, min_len=0):
    if len(arr) == 0:  
        return []
    
    min_len = max(2, min_len)  
    
    start, end = 0, 1  
    min_window = arr  
    
    while end < len(arr):
        if arr[end] > arr[end - 1]:  
            if end - start + 1 >= min_len:  
                if end - start + 1 < len(min_window):  
                    min_window = arr[start:end + 1]
        else:  
            start = end
        end += 1  
    
    return min_window if len(min_window) >= min_len else []