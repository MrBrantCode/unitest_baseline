"""
QUESTION:
Implement the `interpolation_search` function that performs an interpolation search for an element `x` in a sorted array. The function should return the index of the first occurrence of `x` if it exists in the array; otherwise, it returns -1. The function should handle duplicate elements and have a time complexity of O(log log n) in the worst case scenario.
"""

def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high and arr[low] <= x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            else:
                return -1
        
        # Calculate the position of the midpoint
        position = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        # Check if the element is found at the calculated position
        if arr[position] == x:
            # Check for the first occurrence of the element
            while position > 0 and arr[position - 1] == x:
                position -= 1
            return position
        
        # If the element is greater, search the right subarray
        if arr[position] < x:
            low = position + 1
        # If the element is smaller, search the left subarray
        else:
            high = position - 1
    
    return -1