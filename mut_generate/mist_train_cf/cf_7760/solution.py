"""
QUESTION:
Implement a recursive binary search function called `binary_search_helper` that finds the index of the first occurrence of a target element in a sorted array, handling duplicate elements and using constant space complexity. The function should take a sorted array, a target element, and the low and high indices of the search range as parameters. If the target element is not found, the function should return -1.
"""

def binary_search_helper(array, target, low, high):
  if low > high:
    return -1
  
  mid = (low + high) // 2
  
  if array[mid] == target:
    # Handle duplicates
    while mid > low and array[mid - 1] == target:
      mid -= 1
    return mid
  
  if array[mid] < target:
    return binary_search_helper(array, target, mid + 1, high)
  else:
    return binary_search_helper(array, target, low, mid - 1)