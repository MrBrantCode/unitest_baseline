"""
QUESTION:
Implement a function called `bubble_sort` that takes a list of numbers as input and returns the sorted list in ascending order using the bubble sort algorithm.
"""

def bubble_sort(lst):
  for i in range(len(lst)):
   for j in range(len(lst)-1-i):
    if lst[j] > lst[j+1]:
     lst[j], lst[j+1] = lst[j+1], lst[j]
  return lst