"""
QUESTION:
Write a function called `binary_search` that performs a recursive binary search in a sorted array. The function should take four parameters: the sorted array `arr`, the left and right indices `left` and `right`, and the target element `target`. The function should return the index of the target element if it exists in the array, and -1 otherwise.
"""

def binary_search(arr, left, right, target):
    # Check base case 
    if right >= left:
        mid = left + (right - left) // 2 
  
        # If element is present at the middle itself 
        if arr[mid] == target:
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray
        elif arr[mid] > target:
            return binary_search(arr, left, mid-1,target)
       
        # Else the element can only be present  
        # in right subarray
        else:
            return binary_search(arr, mid + 1, right,target) 

    else: 
        # Element is not present in the array 
        return -1