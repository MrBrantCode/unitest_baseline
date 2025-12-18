"""
QUESTION:
Create a function `sortBinaryArray(arr)` that sorts a binary array in-place so that all 0s come before all 1s. The function should modify the input array and return the sorted array.
"""

def sortBinaryArray(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    if arr[start] == 1:
      arr[start], arr[end] = arr[end], arr[start]
      end -= 1
    else:
      start += 1
  return arr