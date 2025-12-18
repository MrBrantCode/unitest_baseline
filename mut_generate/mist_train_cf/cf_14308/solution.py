"""
QUESTION:
Write a function binary_search that implements a recursive binary search algorithm. The function should take four parameters: array, target, low, and high, where array is the list of elements to be searched, target is the element to be found, and low and high are the starting and ending indices of the range to be searched. The function should return the index of the target element if found, and -1 otherwise. The function should use a recursive approach to find the target element.
"""

def binary_search(array, target, low, high):
  if low <= high:
    mid = (low+high)//2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      return binary_search(array, target, mid+1, high)
    else:
      return binary_search(array, target, low, mid-1)
  return -1