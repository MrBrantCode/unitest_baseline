"""
QUESTION:
Implement a function called `binary_search` that takes a sorted array of integers and a target integer as input. The function should return the index of the first occurrence of the target integer in the array, or -1 if it is not present. Assume the array may contain duplicates and the array is sorted.
"""

def binary_search(arr, x): 
    """
    Returns the index of the first occurrence of the target integer in a sorted array.
    
    Parameters:
    arr (list): A sorted list of integers.
    x (int): The target integer to be searched.
    
    Returns:
    int: The index of the first occurrence of the target integer, or -1 if it is not present.
    """
    low = 0
    high = len(arr) - 1
  
    while low <= high: 
        mid = (low + high) // 2
  
        if arr[mid] == x and (mid == 0 or arr[mid - 1] != x): 
            return mid 
  
        elif arr[mid] < x: 
            low = mid + 1
  
        else: 
            high = mid - 1
  
    return -1