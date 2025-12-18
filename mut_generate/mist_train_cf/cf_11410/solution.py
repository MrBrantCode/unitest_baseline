"""
QUESTION:
Implement a function named `interpolation_search` that performs interpolation search on a sorted array. The function should take two parameters: `arr` (a sorted list of elements) and `x` (the target element to be searched). The function should return the index of the target element if found, and -1 if not found. The array is sorted in ascending order.
"""

def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1
        
        position = low + int(((float(high - low) / ( arr[high] - arr[low])) * (x - arr[low])))
        
        if arr[position] == x:
            return position
        
        if arr[position] < x:
            low = position + 1
        else:
            high = position - 1
    
    return -1