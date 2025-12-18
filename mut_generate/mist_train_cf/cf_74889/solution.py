"""
QUESTION:
Write a function `multiply_vectors(a, b)` that performs element-wise multiplication on two input vectors `a` and `b` and returns the resulting vector. The function should handle the case where the input vectors are not of the same dimension and return an error message in this case.
"""

def multiply_vectors(a, b):
  if len(a) != len(b):
    return "The vectors are not of same dimensions."
  
  result = [a[i]*b[i] for i in range(len(a))]
  return result