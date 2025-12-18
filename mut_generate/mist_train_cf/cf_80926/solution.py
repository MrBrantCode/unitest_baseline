"""
QUESTION:
Implement a function named `quinary_search` that takes an array of integers and a target value `x` as input, and returns the index of `x` in the array if found. The function should handle cases where the input array is not sorted or contains duplicates. If `x` is not found, the function should return "Element Not Found".
"""

def quinary_search(arr, x): 
    arr.sort() # To ensure sorted array
    arr = list(dict.fromkeys(arr)) # Removing duplicates if any
    # initializing starting and ending points
    start, end = 0, len(arr) - 1
    while start <= end:
        mid1 = start + (end - start) // 5
        mid2 = mid1 + (end - start) // 5
        mid3 = mid2 + (end - start) // 5
        mid4 = mid3 + (end - start) // 5
  
        if arr[mid1] == x: 
            return mid1 
        if arr[mid2] == x:
            return mid2
        if arr[mid3] == x: 
            return mid3
        if arr[mid4] == x:
            return mid4
        if x < arr[mid1]: 
            end = mid1 - 1
        elif x > arr[mid1] and x < arr[mid2]:
            start, end = mid1 + 1, mid2 - 1 
        elif x > arr[mid2] and x < arr[mid3]:
            start, end = mid2 + 1, mid3 - 1 
        elif x > arr[mid3] and x < arr[mid4]:
            start, end = mid3 + 1, mid4 - 1 
        elif x > arr[mid4]:
            start = mid4 + 1 
            
    return "Element Not Found"  # If element not found 