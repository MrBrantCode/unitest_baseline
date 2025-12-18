"""
QUESTION:
Write a function `find_smallest(arr, start, end)` to find the smallest element in a given array of positive integers using a divide and conquer approach. The array length is between 1 and 100, and the values are between 1 and 1000.
"""

def find_smallest(arr, start, end):
    # If the array contains only one element, return it
    if start == end:
        return arr[start]
    
    # If the array contains two elements, return the smaller one
    if end - start == 1:
        return min(arr[start], arr[end])
    
    # Divide the array into two halves
    mid = (start + end) // 2
    left_min = find_smallest(arr, start, mid)
    right_min = find_smallest(arr, mid + 1, end)
    
    # Compare the smallest elements from both halves and return the minimum
    return min(left_min, right_min)