"""
QUESTION:
Write a function `calcProduct(n, arr)` that calculates the product of each element in the array `arr` raised to the power of `i`, where `i` ranges from 1 to `n`. The function should take a positive integer `n` and a list of positive integers `arr` as input, and return the total product.

Restrictions: `n` is a positive integer and `arr` is a list of positive integers.
"""

def calcProduct(n, arr):
  if len(set(arr)) == 1:   
      return arr[0] ** (n * len(arr))
    
  product = 1
  for i in range(1, n+1):
      for j in range(1, len(arr)+1):
          product *= arr[j-1] ** i
  return product