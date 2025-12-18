"""
QUESTION:
Implement a function called `binary_search` that takes a sorted array `arr` and a target element `x` as input. The function should return the index of the target element if it exists in the array, and -1 otherwise. The array is sorted in ascending order and the function should have a time complexity of O(log n).
"""

def binary_search(arr, x): 
    # find the leftmost and rightmost point 
    l = 0
    r = len(arr) - 1
      
    while l <= r: 
  
        mid = l + (r - l)//2
  
        # if element is present at the middle  
        if arr[mid] == x: 
            return mid 
  
        # if element is smaller than mid,  
        # then it can only be present  
        # in left subarray 
        elif arr[mid] < x: 
            l = mid + 1
  
        # else the element can only  
        # be present in right subarray 
        else: 
            r = mid - 1
      
    # if we reach here,  
    # then the element was not present 
    return -1