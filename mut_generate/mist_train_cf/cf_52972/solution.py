"""
QUESTION:
Create a binary search function named `binary_search` that takes in a list of elements `array` and a target value `target`. The function should return the index of the target value if it exists in the array, and an error message if it does not. The function should handle cases where the array is not sorted, and where the array or target value has an invalid type.
"""

def binary_search(array, target):
  try:
    array = sorted(array)  # ensuring array is sorted
    low = 0
    high = len(array) - 1
    while low <= high:
      mid = (low + high) // 2
      if array[mid] == target:
        return mid
      elif array[mid] < target:
        low = mid + 1
      else:
        high = mid - 1
    return 'Target not found in array'  # if target doesn't exist in array
  except TypeError:
    return 'Array or target value has invalid type'
  except Exception as e:
    return str(e)