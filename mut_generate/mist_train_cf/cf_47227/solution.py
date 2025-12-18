"""
QUESTION:
Create a function `sum_even_elements` that calculates the sum of all even elements in an array of length `n` (1 <= n <= 10^5), where each element is a random integer between 1 and 100. The function should be optimized for performance and accept the array as an input parameter. The array should not be hardcoded and should be dynamically generated.
"""

import numpy as np

def sum_even_elements(arr):
  return np.sum(arr[arr % 2 == 0])