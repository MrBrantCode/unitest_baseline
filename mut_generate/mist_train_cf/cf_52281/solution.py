"""
QUESTION:
Create a function `max_diff(arr)` that finds the maximum difference between two elements in a non-decreasing subarray within a given array `arr` and returns this maximum difference along with the pair of elements that contribute to it. The array `arr` is not necessarily sorted and may contain duplicate elements. The function should handle the case where the array has at least two elements.
"""

def max_diff(arr):
    if not arr:
        return
    min_el = arr[0]
    max_diff = arr[1] - arr[0]
    pair = (arr[0], arr[1])
    
    for i in range(1, len(arr)):
        if arr[i] < min_el:
            min_el = arr[i]  
        elif arr[i] - min_el > max_diff:
            max_diff = arr[i] - min_el
            pair = (min_el, arr[i])
    
    return max_diff, pair