"""
QUESTION:
Write a function `checkReverse(arr1, arr2)` that checks if two input arrays have the same elements in reverse order, regardless of the arrays' lengths and the data types of their elements (which can include integers, strings, and nested arrays).
"""

def checkReverse(arr1, arr2):
  # compare lengths of arrays
  if len(arr1) != len(arr2):
    return False
  # compare each element of arr1 with reverse order element in arr2 
  for i in range(len(arr1)):
    if arr1[i] != arr2[len(arr1)-1-i]:
      return False
  # return true if all elements match in reverse  
  return True