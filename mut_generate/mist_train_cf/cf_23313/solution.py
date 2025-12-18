"""
QUESTION:
Write a function named `binarySearch` that takes in two parameters: `array` and `item`. The `array` is a sorted list of elements, and `item` is the target value to be searched. Implement a binary search algorithm to find the index of the `item` in the `array`. If the `item` is found, return its index; otherwise, return `None`. Assume the `array` index starts at 0.
"""

def binarySearch(array, item):
  low = 0
  high = len(array) - 1

  while low <= high:
    mid = (low + high) // 2
    guess = array[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None