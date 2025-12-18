"""
QUESTION:
Create a function called `max_subarray_sum` that takes a list of numbers as input and returns the maximum subarray sum. The function should use Kadane's algorithm and handle lists containing at least one element.
"""

def max_subarray_sum(numbers):
  
  # Initialize current max and global max
  current_max = numbers[0]
  global_max = numbers[0]
  
  # Loop through all elements in the list starting from index 1
  for i in range(1, len(numbers)):
      current_max = max(numbers[i], current_max + numbers[i])
      if current_max > global_max:
          global_max = current_max

  return global_max