"""
QUESTION:
Write a function `split_array` that takes three parameters: an array `arr`, the number of slices `n`, and the maximum length of each slice `m`. The function should split `arr` into `n` slices, each with a maximum of `m` elements, maintaining the order of elements. If the array cannot be divided evenly, the last slice should contain the remaining elements.
"""

def split_array(arr, n, m):
    slices = []
    slice_length = min(m, len(arr) // n)  # Calculate the length of each slice
    remaining_elements = len(arr) % n  # Calculate the remaining elements
    start = 0
    
    for i in range(n):
        if i < remaining_elements:
            slice = arr[start:start+slice_length+1]  
            start += slice_length + 1
        else:
            slice = arr[start:start+slice_length]  
            start += slice_length
        slices.append(slice)
    return slices