"""
QUESTION:
Implement a recursive binary search function that finds the index of the first occurrence of a target element in a sorted array with duplicate elements. The function, named `binary_search`, should take four parameters: the sorted array, the target element, the lower bound of the search range (low), and the upper bound of the search range (high). If the target element is not found, the function should return -1. The function should handle duplicate elements by returning the index of the first occurrence of the target element.
"""

def binary_search(array, target, low, high):
  if low <= high:
    mid = (low + high) // 2
    if array[mid] == target:
      while mid > low and array[mid - 1] == target:
        mid -= 1
      return mid
    elif array[mid] < target:
      return binary_search(array, target, mid + 1, high)
    else:
      return binary_search(array, target, low, mid - 1)
  return -1