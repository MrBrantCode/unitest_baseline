"""
QUESTION:
Write a function called `loopList` that takes an array `arr` as input. The function should return the sum of the squares of the first 5 elements in the array. If the array has less than 5 elements, the function should recycle the elements. For example, if the array has 3 elements [a, b, c], it should calculate the sum of squares as a^2 + b^2 + c^2 + a^2 + b^2.
"""

def loopList(arr):
  total = sum([arr[i % len(arr)] ** 2 for i in range(5)])
  return total