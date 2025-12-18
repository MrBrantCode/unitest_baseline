"""
QUESTION:
Implement a function `bubble_sort(lst)` that takes a list of numeric strings and numbers as input, sorts the list in ascending order based on numeric representation, and returns the sorted list. The function should handle mixed data types and implement the optimization where if no swapping occurs during a pass, it assumes the list is sorted and halts execution. Each pass should iterate over one less element than the previous pass, as the last elements are already sorted after each pass.
"""

def entrance(lst):
  n = len(lst)
  
  for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
      # Comparing numeric representation of each pair of adjacent elements
      if int(lst[j]) > int(lst[j+1]):
        lst[j], lst[j+1] = lst[j+1], lst[j]
        swapped = True 
  
    # If no elements were swapped, the list is already sorted
    if not swapped:
      break

  return lst