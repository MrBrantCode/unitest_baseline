"""
QUESTION:
Write a function `find_element(arr, target)` that performs a search operation in a sorted and rotated array with a time complexity of O(log n). The array is sorted in ascending order and rotated at an unknown pivot point. The function should return the index of the target element if found; otherwise, it should return a message indicating that the element is not in the array.
"""

def find_element(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if target == arr[mid]:
            return mid
        
        # if the left side is sorted
        if arr[low] <= arr[mid]:
            # target lies within range 
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
                
        else: # if the right side is sorted
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return "The element is not in the array."