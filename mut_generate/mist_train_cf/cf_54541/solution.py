"""
QUESTION:
Design a function `find_top_five_highest_lowest` that takes a list of floating numbers as input and returns two lists: the top five highest values and the bottom five lowest values. The function should handle recurring values, negative numbers, and zeros. Assume the input is a one-dimensional list of floating numbers. Optimize for both time and space complexity.
"""

import heapq

def find_top_five_highest_lowest(dataset):
  # Heapify the dataset
  highest = heapq.nlargest(5, dataset)
  lowest = heapq.nsmallest(5, dataset)

  return highest, lowest