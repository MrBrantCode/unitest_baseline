"""
QUESTION:
Write a function named `divide_array` that takes an array of integers as input and returns two halves of the array. The function should divide the array into two parts as evenly as possible, with any extra element in the case of an odd-length array going to the right half.
"""

def divide_array(arr):
  middle = len(arr) // 2
  return arr[:middle], arr[middle:]