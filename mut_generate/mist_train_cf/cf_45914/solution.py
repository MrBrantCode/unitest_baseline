"""
QUESTION:
Create a function named `insert_to_sorted_array` that takes a sorted array and a number as input. The function should insert the number into the array at the appropriate index to maintain the sorted order, handling duplicate values, negative numbers, and zero. The function should not use any built-in insert function. The output should be the modified sorted array with the number inserted at the correct position.
"""

def insert_to_sorted_array(sorted_array, num):
  for i in range(len(sorted_array)):
    if sorted_array[i] > num:
      sorted_array = sorted_array[:i] + [num] + sorted_array[i:]
      return sorted_array
  return sorted_array + [num]