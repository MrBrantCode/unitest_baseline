"""
QUESTION:
Write a function named `transformArray` that takes an array `arr` of length between 3 and 100 as input and returns the final, unchanging array after a series of transformations. Each transformation increments an element if it's less than both its neighbors, decrements an element if it's greater than both its neighbors, and leaves the first and last elements unchanged. The function should continue applying these transformations until no more changes can be made to the array. The input array `arr` contains integers between 1 and 100.
"""

def transformArray(arr):
  while True:
    orig = arr[:]
    for i in range(1, len(arr)-1):
      if arr[i-1] > arr[i] and arr[i+1] > arr[i]:
        orig[i] += 1
      elif arr[i-1] < arr[i] and arr[i+1] < arr[i]:
        orig[i] -= 1
    if orig == arr:
      break
    else:
      arr = orig

  return arr