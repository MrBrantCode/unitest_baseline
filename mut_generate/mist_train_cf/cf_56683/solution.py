"""
QUESTION:
Create a function called `binary_search` that takes a sorted array of numbers, the low and high indices of the array, and a target number as input. The function should implement a binary search algorithm to find the index of the target number in the array. If the target number is found, return its index; otherwise, return -1. The function should be recursive, dividing the search space in half at each step until the target number is found.
"""

def binary_search(arr, low, high, x):
  
  if high >= low:

    mid = (high + low) // 2

    # If element is present at the middle itself
    if arr[mid] == x:
      return mid

    # If element is smaller than mid, then it can only be present in the left subarray
    elif arr[mid] > x:
      return binary_search(arr, low, mid - 1, x)

    # Else the element can only be present in the right subarray
    else:
      return binary_search(arr, mid + 1, high, x)

  else:
    # Element is not present in the array
    return -1