"""
QUESTION:
Create a function `multiply_by_two` that takes an array as input, multiplies each element by 2, and returns the new array. The function should handle arrays with nested arrays by flattening the array and multiplying each element by 2. The solution should have a time complexity less than O(n^2), where n represents the total number of elements in the array.
"""

def multiply_by_two(arr):
  # Create a queue to hold array values
  queue = list(arr)
  # Create a new array to hold the multiplied values
  result = []

  # Continue until all elements in the array are processed
  while queue:
    value = queue.pop(0)
    # If the value is an array, add its elements to the queue
    if isinstance(value, list):
      queue = value + queue
    # If the value is an integer, double it and add to the result
    else:
      result.append(value * 2)
  
  return result