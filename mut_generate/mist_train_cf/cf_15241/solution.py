"""
QUESTION:
Implement a function named `find_smallest` that uses a divide and conquer approach to find the smallest element in a given array of positive integers, where the array length is between 1 and 100, and the values are between 1 and 1000. The function should take an array and its start and end indices as parameters.
"""

def find_smallest(arr, start, end):
    if start == end:
        return arr[start]
    
    if end - start == 1:
        return min(arr[start], arr[end])
    
    mid = (start + end) // 2
    left_min = find_smallest(arr, start, mid)
    right_min = find_smallest(arr, mid + 1, end)
    
    return min(left_min, right_min)