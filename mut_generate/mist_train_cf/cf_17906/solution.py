"""
QUESTION:
Write a function `quickSort` that sorts an array of numbers from largest to smallest using the quick sort algorithm, with a worst-case time complexity of O(n^2) and a space complexity of O(n). The function should take three parameters: the array to be sorted, and two indices `left` and `right` representing the range of the array to be sorted.
"""

def quickSort(arr, left, right):
  if left >= right:
    return
  
  pivot = arr[right]
  partition_index = left
  
  for i in range(left, right):
    if arr[i] > pivot:
      arr[i], arr[partition_index] = arr[partition_index], arr[i]
      partition_index += 1
  
  arr[partition_index], arr[right] = arr[right], arr[partition_index]
  
  quickSort(arr, left, partition_index - 1)
  quickSort(arr, partition_index + 1, right)