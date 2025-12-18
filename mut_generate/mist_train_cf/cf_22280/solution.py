"""
QUESTION:
Write a function `binary_search` that uses a recursive approach to search for a target element in a sorted array. The function should handle duplicate elements by returning the index of the first occurrence of the target element. The function should take four parameters: the array to be searched, the target element, the lower bound of the search range (low), and the upper bound of the search range (high). The function should return the index of the first occurrence of the target element if found, and -1 otherwise. The array is assumed to be sorted in ascending order.
"""

def binary_search(array, target, low, high):
  if low <= high:
    mid = (low + high) // 2
    if array[mid] == target:
      # Handle duplicates
      while mid > low and array[mid - 1] == target:
        mid -= 1
      return mid
    elif array[mid] < target:
      return binary_search(array, target, mid + 1, high)
    else:
      return binary_search(array, target, low, mid - 1)
  return -1