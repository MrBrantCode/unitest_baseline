"""
QUESTION:
Create a function named `sort_array` that takes an array of integers as input and returns the array sorted in ascending order. The function should be able to handle arrays of any length and containing any integer values. The array should be sorted in-place, meaning that the original array is modified and no additional space is used that scales with the input size.
"""

def sort_array(arr): 
  # Loop through the array, swap each element until it is in order (ascending)
  for i in range(len(arr) - 1): 
    for j in range(i + 1, len(arr)): 
      if arr[i] > arr[j]: 
        temp = arr[i] 
        arr[i] = arr[j] 
        arr[j] = temp 
  
  # Return the sorted array 
  return arr