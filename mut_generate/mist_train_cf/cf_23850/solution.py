"""
QUESTION:
Implement a function `bubbleSort` that takes a list of numbers as input and returns the list sorted in increasing order. The function should use the bubble sort algorithm.
"""

def bubbleSort(arr):
  for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr