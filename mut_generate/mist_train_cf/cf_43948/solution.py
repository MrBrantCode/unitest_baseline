"""
QUESTION:
Create a function named `modify_abs_values_v2` that takes a list of numbers as input and returns the product of the absolute values of these numbers, factoring in only their closest rounded-down integers. Exclude the elements that are divisible by any prime number less than or equal to 10. The function should handle exceptions/errors without crashing and be able to handle large numbers and arrays.
"""

import math

def modify_abs_values_v2(lst):
  try:
    primes = [2, 3, 5, 7]  
    product = 1
    for num in lst:
      num = int(math.floor(math.fabs(num)))  
      if num > 1 and not any(num % i == 0 for i in primes):
        product *= num
    return product
  except TypeError:  
    return "List elements must be numerical values."
  except:
    return "An unexpected error occurred."