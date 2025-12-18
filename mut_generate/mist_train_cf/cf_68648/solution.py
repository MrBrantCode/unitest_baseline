"""
QUESTION:
Create a function `sorting1DArray(arr)` that sorts the input array `arr` in ascending order. The input array can be either a one-dimensional list of numbers or a two-dimensional list (nested list) of numbers. The function should return the sorted list of numbers.
"""

def sorting1DArray(arr):
    # Check if 'arr' is a nested list
    if isinstance(arr[0], list):
        # If true, flatten the list
        arr = [num for sublist in arr for num in sublist]
            
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                
    return arr