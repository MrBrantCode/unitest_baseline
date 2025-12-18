"""
QUESTION:
Write a function called `reverseArray` that takes an array of at least 100 and at most 10,000 elements as input and returns the array with its elements in reverse order. The function should not use any built-in functions or libraries, and it should have a time complexity of O(n), where n is the length of the input array.
"""

def reverseArray(arr):
  for i in range(len(arr) // 2):
    arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
  return arr